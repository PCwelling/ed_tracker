from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from ..login.models import User
from ..people.models import Student
from ..instructor.models import Instructor
from ..agency.models import Agency
from ..store.models import Store
from django.db import models

# Create your models here.
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

class Course_type(models.Model):   
    course_title = models.CharField(max_length=30, validators = [validateLengthGreaterThanTwo])
    desc = models.TextField(max_length=300)
    user = models.ForeignKey(User, related_name="course_types")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.course_title)

class CourseManager(models.Manager):
    
    def remove_from_course(self, post_data):
        course_add = Course.objects.get(id = post_data['course_id'])
        course_add.student.remove(Student.objects.get(id = post_data['student_id']))
        course_add.save()

    def add_to_course(self, post_data):
        course_add = Course.objects.get(id = post_data['course_id'])
        course_add.student.add(Student.objects.get(id = post_data['student_id']))
        course_add.save()       

class Course(models.Model):
    course_type = models.ForeignKey(Course_type, related_name="courses")
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    agency = models.ForeignKey(Agency, related_name="courses")
    store = models.ForeignKey(Store, related_name="courses")
    instructor = models.ManyToManyField(Instructor, related_name="courses")
    student = models.ManyToManyField(Student, related_name="courses")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()