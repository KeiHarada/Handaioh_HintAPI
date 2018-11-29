# coding: utf-8
import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from .models import Node, Hint
from .serializer import NodeSerializer, HintSerializer

class NodeFilter(django_filters.FilterSet):
    fullname = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Node
        fields = "__all__"

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.nodes.all()
    serializer_class = NodeSerializer
    filter_fields = ("node", "rank")
    filter_class = NodeFilter

class HintFilter(django_filters.FilterSet):
    fullname = django_filters.CharFilter(lookup_expr='contains')
    score_gt = django_filters.NumberFilter(lookup_expr='gt')

    class Meta:
        model = Hint
        fields = "__all__"

class HintViewSet(viewsets.ModelViewSet):
    queryset = Hint.nodes.all()
    serializer_class = HintSerializer
    filter_fields = ("node", "rank")
    filter_class = HintFilter

def get_nodes(request):
    return render('http://bd-ensyu.ist.osaka-u.ac.jp:15000/api/nodes', request, {'nodes': Node.nodes.all()})

def get_hints(request):
    return render('http://bd-ensyu.ist.osaka-u.ac.jp:15000/api/nodes', request, {'hints': Hint.nodes.all()})