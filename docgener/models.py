from django.db import models
import datetime

# Create your models here.
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Document(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    document_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.document_name
