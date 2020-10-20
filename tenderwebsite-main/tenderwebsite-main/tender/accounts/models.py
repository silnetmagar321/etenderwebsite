from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from memberships.models import Membership


def upload_location(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, blank=True, null=True)
    contact_person_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    allowed_memberships = models.ManyToManyField(Membership)

    def get_absolute_url(self):
        return reverse("profiles:detail", kwargs={'username': self.user.username})

    def __str__(self):
        return self.user.username
