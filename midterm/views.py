from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from midterm.models import MediaEntry, User, MediaCheckout
from midterm.forms import UpdateCartForm
import datetime

def name_to_url(name):
    return name.replace(' ', '_')

def decode_url(url):
    return url.replace('_', ' ')

# Create your views here.

from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    title_result = []
    isbn_result = []
    topic_result = []
    subtopic_result = []
    user_list = []
    user_list = User.objects.all()
    selected_user = ""
    
    if request.method == 'POST':
        query = request.POST['query'].strip()
        user = request.POST['user'].strip()
        
        if query:
            title_result = MediaEntry.objects.filter(name__icontains = query)
            isbn_result = MediaEntry.objects.filter(isbn__icontains = query)
            topic_result = MediaEntry.objects.filter(media_topic__name__icontains = query)
            subtopic_result = MediaEntry.objects.filter(media_subtopic__name__icontains = query)
        else:
            title_result = MediaEntry.objects.all()
            isbn_result = MediaEntry.objects.all()
            topic_result = MediaEntry.objects.all()
            subtopic_result = MediaEntry.objects.all()

        if user:
            selected_user = User.objects.get(id=user)

    return render(request, 'midterm/index.html', {'selected_user': selected_user, 'user_list': user_list, 'title_result': title_result, 'isbn_result': isbn_result, 'topic_result': topic_result, 'subtopic_result': subtopic_result}, context)

def addcart(request, user_id, entry_id):
    context = RequestContext(request)

    user = User.objects.get(id=user_id)
    entry = MediaEntry.objects.get(id=entry_id)

    today = datetime.date.today()
    delta = datetime.timedelta(days=7)
    due_date = today + delta

    checkout = MediaCheckout(media_entry=entry, user=user, checkout_date=today, due_date=due_date)
    checkout.save()

    checkout_entry = MediaCheckout.objects.filter(user__id = user_id)

    return render(request, 'midterm/viewcart.html', {'selected_user': u, 'checkout_entry': checkout_entry}, context)

def viewcart(request, user_id):
    context = RequestContext(request)

    user = User.objects.get(id=user_id)
    checkout_entry = MediaCheckout.objects.filter(user__id = user_id)

    return render(request, 'midterm/viewcart.html', {'selected_user': user, 'checkout_entry': checkout_entry}, context)

def entry(request, entry_id):
    context = RequestContext(request)
    entry = MediaEntry.objects.get(id=entry_id)
    
    return render(request, 'midterm/entry.html', {'entry': entry}, context)

def cart(request):
    context = RequestContext(request)
    user_list = []
    user_list = User.objects.all()
    entry_result = []
    query_result = ""
    
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            entry_result = MediaCheckout.objects.filter(user__name = query)
            query_result = query

    return render(request, 'midterm/cart.html', {'query_result': query_result, 'user_list': user_list, 'entry_result': entry_result, }, context)

def update_cart(request, cart_id):
    context = RequestContext(request)
    entry = MediaCheckout.objects.get(id=cart_id)

    if request.method == 'POST':
        form = UpdateCartForm(request.POST)

    else:
        form = UpdateCartForm()
        #form = UpdateCartForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'midterm/update_cart.html', {'form': form, 'entry': entry}, context)

"""def about(request):
    #return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/about.html', context_dict, context)
def category(request, category_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)
    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    category_name = category_name_url.replace('_', ' ')
    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'category_name': category_name}
    context_dict['category_name_url'] = category_name_url
    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass
        # Go render the response and return it to the client.
    return render_to_response('rango/category.html', context_dict, context)
@login_required
def add_category(request):
    # Get the context from the request.
    context = RequestContext(request)
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    #return render_to_response('rango/add_category.html', {'form': form}, context)
    return render(request, {'form': form}, context)
@login_required
def add_page(request, category_name_url):
    context = RequestContext(request)
    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            page = form.save(commit=False)
            # Retrieve the associated Category object so we can add it.
            cat = Category.objects.get(name=category_name)
            page.category = cat
            # Also, create a default value for the number of views.
            page.views = 0
            # With this, we can then save our new model instance.
            page.save()
            # Now that the page is saved, display the category instead.
            return category(request, category_name_url)
        else:
            print (form.errors)
    else:
        form = PageForm()
        #return render_to_response('rango/add_page.html', {'category_name_url': category_name_url, 'category_name': category_name, 'form': form}, context)
        return render(request, 'rango/add_page.html', {'category_name_url': category_name_url, 'category_name': category_name, 'form': form}, context)
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                # Now we save the UserProfile model instance.
                profile.save()
                # Update our variable to tell the template registration was successful.
                registered = True
                
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)
            # Not a HTTP POST, so we render our form using two ModelForm instances.
            # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered':registered}, context)
def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html', {}, context)
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')
"""
