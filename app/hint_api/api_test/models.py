# coding: utf-8
from django.db import models

class Hint(models.Model):
    node = models.CharField(max_length=256)
    hint = models.TextField()
    rank = models.PositiveSmallIntegerField(default=0)
