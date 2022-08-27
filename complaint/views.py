
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Complaint
from .serializers import ComplaintSerializer

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
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # List all the Complains.
    def get(self, request):
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)
