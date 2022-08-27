
from rest_framework import serializers
from .models import Complaint


# Serializer for Complaints 
class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = [
            "id",
            "subject",
            "description",
            "user",
            "complaint_status",
            "created_at",
            "updated_at",
        ]
