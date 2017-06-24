from django import forms
#from django.contrib.auth.models import User
from midterm.models import MediaCheckout
import datetime

class UpdateCartForm(forms.Form):
    checkout_date = forms.DateField()
    due_date = forms.DateField()
    return_date = forms.DateField()
    renewal_date = forms.DateField()
    overdue_fine = forms.IntegerField(initial=0)
    
    """name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)"""

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        #model = Cart
        fields = ['checkout_date', 'due_date', 'return_date', 'renewal_date', 'overdue_fine']
        #fields = ['name']


