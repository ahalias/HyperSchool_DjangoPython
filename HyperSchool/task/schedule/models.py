from django.db import models
from django.shortcuts import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.TextField()

    def get_absolute_url(self):
        return reverse('teacher_url', kwargs={'id': self.id})

class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=1000)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField("Teacher")

    def get_absolute_url(self):
        return reverse('course_url', kwargs={'id': self.id})

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField("Course")
