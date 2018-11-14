from django.contrib import admin
from .models import Hint
# Register your models here.

@admin.register(Hint)
class Hint(admin.ModelAdmin):
    pass
