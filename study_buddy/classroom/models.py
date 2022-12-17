from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model, get_user
from django.db import models
from django.contrib.auth.models import User
from study_buddy.members.models import AppUser, Profile

UserModel = get_user_model()


# Create your models here.



class Location(models.Model):
    city = models.CharField(
        max_length=40,
    )

    address = models.CharField(
        max_length=200,
    )

    post_code = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return self.city


class Event(models.Model):
    str_fields = ('photo',)
    name = models.CharField(
        'Event Name',
        max_length=40,

    )
    event_date = models.DateTimeField(
        'Event Date & Time',
    )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        blank=True,
    )
    phone = models.CharField(
        max_length=20,
    )
    email_address = models.EmailField(
        'Email Address'
    )

    photo = CloudinaryField('photo',
                            null=True,
                            blank=True,)

    def __str__(self):
        return self.name


def logged_user(request):
    current_user = request.user
    return current_user


class JoinedEvent(models.Model):
    student = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student.profile.first_name} {self.student.profile.last_name} - {self.event}"


class Comment(models.Model):
    description = models.CharField(
        'Comment',
        max_length=150,
    )
    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    event_c = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    user_c = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user_c