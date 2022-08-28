

from django.urls import path
from .views import AllComplaints, ComplaintView, ReviewComplaintView, ChartCountUserComplaints


urlpatterns = [
    path("complaint/",ComplaintView.as_view()),       # create , get 
    
    # Admin access only
    path("admin-review-complaint/",ReviewComplaintView.as_view()),       # Admin(Worker)  update
    
    # Charts Data Endpoints.
    path("chart/user-complaint-count/",ChartCountUserComplaints.as_view()),
    path("chart/all-complaint/",AllComplaints.as_view()),
]