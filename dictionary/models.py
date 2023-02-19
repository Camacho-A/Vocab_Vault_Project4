from django.db import models

# Create your models here.


class Dictionary(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=100)
    partOfSpeech = models.CharField(max_length=100)
    definition = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
