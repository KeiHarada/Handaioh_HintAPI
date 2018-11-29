# coding: utf-8
from rest_framework import serializers
from .models import Node, Hint

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('name')

class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ('name', 'resource', 'rank', 'score')