from __future__ import unicode_literals
from django.core.exceptions import ValidationError
import re
from django.db import models
from ..login.models import User

# # Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')
PHONE_REGEX = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

def validateEmail(value):
    if not re.match(EMAIL_REGEX, value):
        raise ValidationError(
            '{} is an invalid email'.format(value)
        )

    #     # check name fields for letter characters            
    #     if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
    #         errors.append('name fields must be letter characters only')
    #     # check emailness of email
    #     if not re.match(EMAIL_REGEX, post_data['email']):
    #         errors.append("invalid email")
    #     # check uniqueness of email
    #     if len(User.objects.filter(email=post_data['email'])) > 0:
    #         errors.append("email already in use")
    #     # check for a valid phone number
    #     if not re.match(PHONE_REGEX, post_data['phone']):
    #         errors.append("invalid phone number")
    #     # check dob is not in the future
    #     if post_data['dob'] == "":
    #         errors.append("Date of birth is required")
    #     else:
    #         dob = datetime.datetime.strptime(post_data['dob'],"%Y-%m-%d")
    #         if dob > datetime.datetime.today():
    #             errors.append("Date of birth must be in the past")


class Agency(models.Model):   
    agency_name = models.CharField(max_length=30, validators = [validateLengthGreaterThanTwo])
    phone = models.IntegerField()
    email = models.EmailField(max_length=50, validators = [validateEmail])
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    user = models.ForeignKey(User, related_name="agencys")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.agency_name)