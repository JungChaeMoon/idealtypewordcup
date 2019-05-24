
# Create your models here.
from django.db import models
from django_random_queryset import RandomManager


class Contest(models.Model):

    worldcup_name = models.CharField(max_length=100)

    def __str__(self):
        return self.worldcup_name


class Candidate(models.Model):

    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
