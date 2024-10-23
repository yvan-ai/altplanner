# admin_custom/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Utilisateur
from .serializers import CustomUserSerializer


class AddUserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
