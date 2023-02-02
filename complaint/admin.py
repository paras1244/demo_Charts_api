
from django.contrib import admin
from .models import Complaint, ParasPostSave

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


admin.site.register(ParasPostSave)
# class ParasPostSaveAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "user",
#         "subject",
#         "description",
#         "complaint_status",
#         "created_at",
#         "updated_at",
#     ]
# 