from django.contrib import admin
from .models import CreateApplication

@admin.register(CreateApplication)
class CreateApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'recruiter', 'location', 'job_type', 'deadline', 'created_at')
    search_fields = ('title', 'recruiter__username')
    list_filter = ('location', 'job_type', 'deadline')
