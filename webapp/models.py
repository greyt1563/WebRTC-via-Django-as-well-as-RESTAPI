# Create your models here.
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class ContactModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    msg = models.TextField(default="")
    date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.name

