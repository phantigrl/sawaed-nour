from django.contrib import admin
from .models import ContactMessage

from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'submitted_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'service', 'submitted_at')
    search_fields = ('full_name', 'email', 'service')
    list_filter = ('service', 'submitted_at')
