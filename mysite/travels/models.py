from email.policy import default
from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

class Travel(models.Model):
    title=models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    start_of_the_trip = models.DateTimeField()
    end_of_the_trip = models.DateTimeField()
    expense = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("travel", kwargs={"travel_id": self.pk})

class Category(models.Model):
    title=models.CharField(max_length=100 , db_index=True) 

    def __str__(self):
        return self.title