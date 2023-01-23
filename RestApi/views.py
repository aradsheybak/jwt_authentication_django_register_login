from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from User.models import User


class Register(APIView):

    def post(self, request):
        data = request.data
        if data['password'] != data['password_confirm']:
            return Response(
                {'status': status.HTTP_400_BAD_REQUEST, 'message': 'password and confirm password is not match!'})

        serializer_s = UserSerializer(data=request.data)

        if serializer_s.is_valid():
            serializer_s.save()
            return Response({'status': status.HTTP_200_OK, 'message': 'User created', 'data': serializer_s.data})

        return Response({'message': 'Failed', 'error': serializer_s.errors, 'status': status.HTTP_400_BAD_REQUEST})


