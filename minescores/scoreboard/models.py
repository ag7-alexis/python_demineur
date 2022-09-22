from django.db import models

class SizeName(models.TextChoices):
    BEGINNER = 'BEGINNER', 'débutant'
    INTERMEDIATE = 'INTERMEDIATE', 'intérmédiraire'
    EXPERT = 'EXPERT', 'expert'


class User(models.Model):
    email_address = models.fields.EmailField()
    name = models.fields.CharField(max_length=100)


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.fields.DateTimeField()
    time = models.fields.IntegerField()
    width = models.fields.IntegerField()
    height = models.fields.IntegerField()
    count_mine = models.fields.IntegerField()


class Size(models.Model):
    name = models.CharField(max_length=30, choices=SizeName.choices)
    width = models.fields.IntegerField()
    height = models.fields.IntegerField()
    count_mine = models.fields.IntegerField()
