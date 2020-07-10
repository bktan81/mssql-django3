from django.contrib import admin
from django.utils import timezone
from .models import (
    Tag,
)
import datetime, pytz
from django import forms
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings


class TagAdmin(admin.ModelAdmin):
    title = "Tags"
    fieldsets = (
        (None, {"fields": ("tag_address", "description", "status", )}),
    )

    list_display = ("tag_address", "description", "status","get_time_ago", "last_seen","created_at", )

    list_filter = ("status",)

    search_fields = ('tag_address','description')

    def get_time_ago(self, obj):
        obj.last_seen
    get_time_ago.short_description = "Time ago"

admin.site.register(Tag, TagAdmin)