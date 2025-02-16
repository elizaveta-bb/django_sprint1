from django.db import models


class Post(models.Model):
    location = models.CharField(max_length=200)
    date = models.DateField()
    category = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.location
