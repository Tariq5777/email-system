from argparse import ONE_OR_MORE
from django.db import models

# Create your models here.

class Mail(models.Model):
    rEmail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()
