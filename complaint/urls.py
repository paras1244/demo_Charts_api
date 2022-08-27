

from django.urls import path
from .views import ComplaintView, ReviewComplaintView


urlpatterns = [
    path("complaint/",ComplaintView.as_view()),       # create , get 
    
    # Admin access only
    path("admin-review-complaint/",ReviewComplaintView.as_view()),       # Admin(Worker)  update
]