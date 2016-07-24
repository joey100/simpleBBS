from django.db import models
from bbs.models import UserProfile
# Create your models here.

class WebGroup(models.Model):
    name = models.CharField(max_length=64)
    brief = models.CharField(max_length=255,blank=True,null=True)
    owner = models.ForeignKey(UserProfile)
    admins = models.ManyToManyField(UserProfile,blank=True,related_name="group_admins")
    members = models.ManyToManyField(UserProfile,blank=True,related_name="group_members")
    max_members = models.IntegerField(default=200)

    def __str__(self):
        return self.name

'''

class UserProfile(models.Model):
    #for web qq
    friends = models.ManyToManyField('self',related_name="my_friends",blank=True)

    def __str__(self):
        return self.name
'''
