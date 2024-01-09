from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer,ProductSerializer
from rest_framework import viewsets
from api.models import Product
from rest_framework import serializers

class SignUpView(APIView):
    def post(self,request,*args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
class ProductView(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
        
