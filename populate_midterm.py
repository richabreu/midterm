import os

def populate():
    
    rich_user = add_user("Rich")
    kristin_user = add_user("Kristin")
    roman_user = add_user("Roman")

    dvd_mediatype = add_mediatype("DVD")
    bluray_mediatype = add_mediatype("Blu-ray")
    book_mediatype = add_mediatype("Book")
    magazine_mediatype = add_mediatype("Magazine")
    newspaper_mediatype = add_mediatype("Newspaper")

    americanhistory_mediatopic = add_mediatopic("American History")
    religion_mediatopic = add_mediatopic("Religion")
    politics_mediatopic = add_mediatopic("Politics")
    scifi_mediatopic = add_mediatopic("Sci-Fi")

    revolution_mediasubtopic = add_mediasubtopic("American Revolution")
    civilwar_mediasubtopic = add_mediasubtopic("Civil War")

    turn1_mediaentry = add_mediaentry(name="Turn: Washington's Spies Season 1",
                                      isbn="",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/81PvqTsCAkL._SY445_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=dvd_mediatype)
    
    turn2_mediaentry = add_mediaentry(name="Turn: Washington's Spies Season 2",
                                      isbn="",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/81anF3IylBL._SY445_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=dvd_mediatype)

    turn3_mediaentry = add_mediaentry(name="Turn: Washington's Spies Season 3",
                                      isbn="",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/81%2BWievkpiL._SY445_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=dvd_mediatype)

    secretsix_mediaentry = add_mediaentry(name="George Washington's Secret Six",
                                      isbn="0143130609",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/51OngnSX5dL._SX281_BO1,204,203,200_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=book_mediatype)

    seventeenseventysix_mediaentry = add_mediaentry(name="1776",
                                      isbn="0743226720",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/51ctyoISRHL._SX328_BO1,204,203,200_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=book_mediatype)

    johnadams1_mediaentry = add_mediaentry(name="John Adams",
                                      isbn="0743223136",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/517oIyvrNDL._SX325_BO1,204,203,200_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=book_mediatype)

    johnadams2_mediaentry = add_mediaentry(name="John Adams",
                                      isbn="",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/91-r7Xwd69L._SY445_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=revolution_mediasubtopic,
                                      media_type=dvd_mediatype)

    killerangels_mediaentry = add_mediaentry(name="The Killer Angels: A Novel of the Civil War",
                                      isbn="0679643249",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/51z1pK-FFXL._SX331_BO1,204,203,200_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=civilwar_mediasubtopic,
                                      media_type=book_mediatype)

    godsgenerals1_mediaentry = add_mediaentry(name="Gods and Generals",
                                      isbn="0345404920",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/5162SQT9grL._SX320_BO1,204,203,200_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=civilwar_mediasubtopic,
                                      media_type=book_mediatype)

    godsgenerals2_mediaentry = add_mediaentry(name="Gods and Generals",
                                      isbn="",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/81117ESxzZL._SY445_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=civilwar_mediasubtopic,
                                      media_type=dvd_mediatype)

    gettysburg_mediaentry = add_mediaentry(name="Gettysburg",
                                      isbn="",
                                      picture="https://images-na.ssl-images-amazon.com/images/I/81117ESxzZL._SY445_.jpg",
                                      media_topic=americanhistory_mediatopic,
                                      media_subtopic=civilwar_mediasubtopic,
                                      media_type=dvd_mediatype)

    add_mediacheckout(media_entry=gettysburg_mediaentry,
                      user=rich_user,
                      checkout_date="2017-06-05",
                      due_date="2017-06-12",
                      return_date="2017-06-19",
                      overdue_fine="7")

    add_mediacheckout(media_entry=godsgenerals1_mediaentry,
                      user=rich_user,
                      checkout_date="2017-05-19",
                      due_date="2017-05-26",
                      return_date="2017-06-19",
                      overdue_fine="21")

def add_user(name):
    u = User.objects.get_or_create(name=name)[0]
    return u

def add_mediatype(name):
    y = MediaType.objects.get_or_create(name=name)[0]
    return y

def add_mediatopic(name):
    o = MediaTopic.objects.get_or_create(name=name)[0]
    return o

def add_mediasubtopic(name):
    s = MediaSubTopic.objects.get_or_create(name=name)[0]
    return s

def add_mediaentry(name, isbn, picture, media_topic, media_subtopic, media_type):
    e = MediaEntry.objects.get_or_create(name=name, isbn=isbn, picture=picture, media_topic=media_topic, media_subtopic=media_subtopic, media_type=media_type)[0]
    return e

def add_mediacheckout(media_entry, user, checkout_date, due_date, return_date, overdue_fine):
    c = MediaCheckout.objects.get_or_create(media_entry=media_entry, user=user, checkout_date=checkout_date, due_date=due_date, return_date=return_date, overdue_fine=overdue_fine)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting midterm population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'midterm.settings')
    import django
    django.setup()
    from midterm.models import User, MediaType, MediaTopic, MediaSubTopic, MediaEntry, MediaCheckout
    populate()
