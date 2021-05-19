from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    title = models.CharField(max_length=256)
    img = models.ImageField(upload_to='campaign/', null=True)
    privacy = models.BooleanField(default=True)
    description = models.TextField()
    creator = models.OneToOneField(User, related_name="owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField(upload_to='card/', null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=256)
    card = models.ForeignKey("dashboard.Card", related_name="tags", on_delete=models.CASCADE)
    campaign = models.ForeignKey("dashboard.Campaign", related_name="tags", on_delete=models.CASCADE)

    def __str__(self):
        return self.tag


class Note(models.Model):
    note = models.TextField()
    privacy = models.BooleanField(default=False)
    order = models.IntegerField()

    def __str__(self):
        return self.note
