from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "due_date", "user")
    search_fields = ("title", "status")
    list_filter = ("status", "due_date")


