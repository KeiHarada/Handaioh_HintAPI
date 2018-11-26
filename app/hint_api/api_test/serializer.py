# coding: utf-8

from rest_framework import serializers
from .models import Node, Hint

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = "__all__"