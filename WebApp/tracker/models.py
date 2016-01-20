from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activities(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "Activities"

class Fields(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "Fields"

class Subfields(models.Model):
    field = models.ForeignKey(Fields)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "Subfields"

class ActivityFieldEffects(models.Model):
    activity = models.ForeignKey(Activities)
    field = models.ForeignKey(Fields)
    effect = models.FloatField()
    class Meta:
        db_table = "ActivityFieldEffects"

class ActivitySubfieldEffects(models.Model):
    activity = models.ForeignKey(Activities)
    subfield = models.ForeignKey(Subfields)
    effect = models.FloatField()
    class Meta:
        db_table = "ActivitySubfieldEffects"

class UserActivities(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activities)
    class Meta:
        db_table = "UserActivities"

class UserFields(models.Model):
    user = models.ForeignKey(User)
    field = models.ForeignKey(Fields)
    score = models.FloatField()
    class Meta:
        db_table = "UserFields"

class UserSubfields(models.Model):
    user = models.ForeignKey(User)
    subfield = models.ForeignKey(Subfields)
    score = models.FloatField()
    class Meta:
        db_table = "UserSubfields" 

#class UserActivityLogs(models.Model):
#    date = models.DateField()
#    activity = models.ForeignKey(Activities)
#    user = models.ForeignKey(User)
#    class Meta:
#        db_table = "UserActivityLogs"
#
#class UserFieldProgress(models.Model):
#    date = models.DateField()
#    user = models.ForeignKey(User)
#    field = models.ForeignKey(Fields)
#    score = models.FloatField()
#    class Meta:
#        db_table = "UserFieldProgress"
#    
#class UserSubfieldProgress(models.Model):
#    date = models.DateField()
#    user = models.ForeignKey(User)
#    field = models.ForeignKey(Subfields)
#    score = models.FloatField()
#    class Meta:
#        db_table = "UserSubfieldProgress"
