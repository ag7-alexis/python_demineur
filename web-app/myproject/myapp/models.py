from django.db import models


class User(models.Model):
    name = models.fields.CharField(max_length=100)
