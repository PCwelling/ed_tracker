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

# class StudentManager(models.Manager):

    # def validate_student(self, post_data):
    #     errors = []
    #     # check length of name fields
    #     if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
    #         errors.append("name fields must be at least 3 characters")
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


    #     if not errors:
    #         # make our new user

    #         new_student = self.create(
    #             first_name=post_data['first_name'],
    #             middle_initial=post_dat['middle_initial'],
    #             last_name=post_data['last_name'],
    #             dob=post_data['dob'],
    #             sex=post_data['sex'],
    #             phone=post_data['phone'],
    #             email=post_data['email'],
    #             address_1 = post_data['address_1'],
    #             address_2 = post_dat['address_2'],
    #             city = post_data['city'],
    #             state = post_data['state'],
    #             zip_code = post_data['zip_code'],
    #         )
    #         return new_student
    #     return errors

class Student(models.Model):   
    first_name = models.CharField(max_length=30, validators = [validateLengthGreaterThanTwo])
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=30, validators = [validateLengthGreaterThanTwo])
    birth_date = models.DateField(auto_now=False)
    sex = models.CharField(max_length=6)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50, validators = [validateEmail])
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    user = models.ForeignKey(User, related_name="students")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    # objects = StudentManager()