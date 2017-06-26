from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    owner = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=100)
    depth = models.IntegerField()
    level = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name