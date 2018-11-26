#from django.db import models
from neo4django.db import models

# Create your models here.
class Node(models.NodeModel):
    name = models.StringProperty()

class Hint(models.NodeModel):
    name = models.StringProperty()
    score = models.Relationship(Node, rel_type="hint", related_name="score")
    rank = models.Relationship(Node, rel_type="hint", related_name="rank")