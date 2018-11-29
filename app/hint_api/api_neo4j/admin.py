from django.contrib import admin
from .models import Node, Hint
# Register your models here.

@admin.register(Node)
class Node(admin.ModelAdmin):
    pass

@admin.register(Hint)
class Hint(admin.ModelAdmin):
    pass