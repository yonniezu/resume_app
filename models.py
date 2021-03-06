from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import (
    CharField,
    OneToOneField,
    IntegerField,
    Model,
    DateTimeField,
    TextField,
    ForeignKey,
    BooleanField

)

class UserProfile(Model):
    wechat_username = CharField(max_length=80, null=True, blank=True)
    user = models.OneToOneField(User, related_name="user_profile")
    phone_number = IntegerField(default=0, blank=True, null=True)


class JobExperience(Model):
    company_name = CharField(max_length=180, null=True, blank=True)
    title = CharField(max_length=180, null=True, blank=True)
    start_date = DateTimeField(blank=True, null=True)
    end_date = DateTimeField(blank=True, null=True)
    description = TextField(null=True, blank=True)
    user = ForeignKey(User, related_name="job_experiences",
                      null=True, blank=True)
    isCurrent = BooleanField(default=False)
