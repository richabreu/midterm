from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class MediaType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class MediaTopic(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class MediaSubTopic(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    def __unicode__(self):
        return self.name

class MediaEntry(models.Model):
    name = models.CharField(max_length=128)
    isbn = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    media_topic = models.ForeignKey(MediaTopic)
    media_subtopic = models.ForeignKey(MediaSubTopic)
    media_type = models.ForeignKey(MediaType)
    
    def __unicode__(self):
        return self.name

class MediaCheckout(models.Model):
    media_entry = models.ForeignKey(MediaEntry)
    user = models.ForeignKey(User)
    checkout_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(default=0)
    overdue_fine = models.IntegerField(default=0)

    def __unicode__(self):
        return self.media_entry
