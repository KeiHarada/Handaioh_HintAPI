# coding: utf-8
from django_neomodel import DjangoNode
from neomodel import StringProperty, IntegerProperty, FloatProperty

class Node(DjangoNode):
    name = StringProperty()

    class Meta:
        app_label = 'Node'

class Hint(DjangoNode):
    name = StringProperty()
    resource = StringProperty()
    rank = IntegerProperty()
    score = FloatProperty()

    class Meta:
        app_label = 'Hint'

    #hint = models.ForeignKey("Node", related_name="hint")
