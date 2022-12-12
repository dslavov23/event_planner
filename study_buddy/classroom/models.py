from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Homework(models.Model):
    subject = models.CharField(
        max_length=30,
    )
    homework_url = models.URLField()

    def __str__(self):
        return self.subject


class School(models.Model):
    name = models.CharField(
        max_length=40,
    )

    address = models.CharField(
        max_length=200,
    )

    post_code = models.CharField(
        max_length=10,
    )
    phone = models.CharField(
        max_length=20,
    )
    email_address = models.EmailField(
        'Email Address'
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(
        'Event Name',
        max_length=40,

    )
    event_date = models.DateTimeField(
        'Event Date',
    )
    school = models.ForeignKey(
        School,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    teacher = models.CharField(
        max_length=40,
    )
    description = models.TextField(
        blank=True,
    )
    event_url = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
