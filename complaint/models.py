
from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    subject = models.TextField(null=False)
    description = models.TextField(null=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    COMPLAINT_STATUS_CHOICES = (
        ('PROGRESS', 'Work in Progress'),
        ('COMPLETED', 'Completed'),
    )
    complaint_status = models.CharField(max_length=16, choices=COMPLAINT_STATUS_CHOICES, default="PROGRESS")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # need to write unique together with user_id and subject of Complain
    class Meta:
        unique_together = ('user', 'subject', 'complaint_status')
    
    def __str__(self):
        return str(self.id + " : " + self.subject)