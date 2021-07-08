from django.db import models

from petstagram.pets.models import Pet


class Comment(models.Model):
    comment = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

