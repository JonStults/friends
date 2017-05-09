from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=45, null=True, blank = True)
    alias = models.CharField(max_length=45, null=True, blank=True)
    email = models.EmailField(max_length=45, null=True, blank=True)
    password = models.CharField(max_length=45)
    date_of_birth = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#
#
# # class Others(models.Model):
# #     user_id = models.ForeignKey(Users)
#
class Friends(models.Model):
    user_id = models.ForeignKey(Users, null = True, blank = True)
    friend_id = models.ForeignKey(Users, related_name = 'friend', null = True, blank = True)
