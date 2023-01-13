from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ResumeManager(models.Manager):
    def new(self):
        return self.order_by('-id')


class Resume(models.Model):
    name = models.TextField(max_length=200)
    surname = models.TextField(max_length=200)
    email = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=15)
    college = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='img/')
    objects = ResumeManager()
    # graduation_year = models.TextField(max_length=6) #date
    # relevant_courses = models.TextField()
