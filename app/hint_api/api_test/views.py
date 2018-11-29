# coding: utf-8
import django_filters
from rest_framework import viewsets
from .models import Hint
from .serializer import HintSerializer

class HintFilter(django_filters.FilterSet):

    fullname = django_filters.CharFilter(lookup_expr='contains')
    score_gt = django_filters.NumberFilter(lookup_expr='gt')

    class Meta:
        model = Hint
        fields = ["node", "rank"]


class HintViewSet(viewsets.ModelViewSet):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer
    filter_fields = ("node", "rank")
    filter_class = HintFilter