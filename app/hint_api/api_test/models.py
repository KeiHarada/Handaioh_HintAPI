from django.db import models
#from neo4django.db import models

# Create your models here.
class Hint(models.Model):
    node = models.CharField(max_length=256)
    hint = models.TextField()
    rank = models.PositiveSmallIntegerField(default=0)

#class Node(models.NodeModel):
#    name = models.StringProperty()
#
#class Hint(models.NodeModel):
#    name = models.StringProperty()
#    score = models.Relationship(Node, rel_type="hint", related_name="score")
#    rank = models.Relationship(Node, rel_type="hint", related_name="rank")
