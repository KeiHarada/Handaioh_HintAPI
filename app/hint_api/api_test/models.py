from django.db import models

# Create your models here.
class Hint(models.Model):
    node = models.CharField(max_length=256)
    hint = models.TextField()
    rank = models.PositiveSmallIntegerField(default=0)