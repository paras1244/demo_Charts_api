
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Complaint, ParasPostSave
from .serializers import ComplaintSerializer
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ComplaintView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        data = request.data
        data['user'] = request.user.id          # updating RequestData and adding user(FK) -> Request.user
        
        serializer = ComplaintSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        complaints = Complaint.objects.filter(user = request.user)
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)
    

class ReviewComplaintView(APIView):
    permission_classes = (IsAdminUser,)
    
    def put(self, request):
        complaint = Complaint.objects.get(id = request.data.get("complaint_id"))
        serializer = ComplaintSerializer(complaint , data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # List all the Complains.
    def get(self, request):
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# Chart APIS
# Passing data : complaints of perticuler user with % of solved complaints.
class ChartCountUserComplaints(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        users = User.objects.filter(is_staff=False, is_superuser=False)         # fetching only Simple users
        data = []
        for user in users:
            user_complaint = Complaint.objects.filter(user = user)
            if user_complaint.exists():
                data.append({
                    "user" : user.id,
                    "total_complaint" : Complaint.objects.filter(user = user).count(),
                    "solved_complaint" : round(Complaint.objects.filter(user=user, complaint_status="COMPLETED").count() / Complaint.objects.filter(user = user).count() * 100, 2)
                })
            else:
                data.append({
                    "user" : user.id,
                    "total_complaint" : Complaint.objects.filter(user = user).count(),
                    "solved_complaint" : "--"
                })
        return Response(data, status=status.HTTP_200_OK)


# Passing the data of solved and in_progress complaints.
class AllComplaints(APIView):
    permission_classes = (AllowAny,)
    
    def get(Self, request):
        data = []
        data.append({
                "total_complaints" : Complaint.objects.all().count(),
                "in_progress" : Complaint.objects.filter(complaint_status="PROGRESS").count(),
                "completed" : Complaint.objects.filter(complaint_status="COMPLETED").count(),
                "solved_percantage" : round(Complaint.objects.filter(complaint_status="COMPLETED").count() / Complaint.objects.all().count() * 100, 2),
                "solved_percantage_str" : str(round(Complaint.objects.filter(complaint_status="COMPLETED").count() / Complaint.objects.all().count() * 100, 2)) + " %",
            })
        return Response(data, status=status.HTTP_200_OK)



@receiver(post_save, sender=Complaint)
def create_validation_rule(sender, instance, **kwargs):
    # print(instance, instance.subject, "----", instance.id, type(instance))
    # print(sender)
    # print(kwargs)

    CODE_CHOICE = [
            ["QRV001",],
            ["QRV002",],
            ["QRV003",],
            ["QRV004",],
            ["QRV005",],
            ["QRV006",],
            ["QRV007",],
            ["QRV008",],
            ["QRV009",],
            ["QRV010",]
        ]
    
    for code in CODE_CHOICE:
        print(code[0])
        ParasPostSave.objects.create(complaint=instance, validation_code=code[0])