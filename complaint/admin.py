
from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "subject",
        "description",
        "complaint_status",
        "created_at",
        "updated_at",
    ]
