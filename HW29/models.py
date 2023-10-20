from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
