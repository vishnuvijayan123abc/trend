from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer,ProductSerializer,BacketItemSerializer,BasketSerializer
from rest_framework import viewsets
from api.models import Product
from rest_framework import serializers
from rest_framework import authentication,permissions
from rest_framework.decorators import action

class SignUpView(APIView):
    def post(self,request,*args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
class ProductView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("permission denied")
    @action(methods=["post"],detail=True)
    def add_to_basket(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        product_obj=Product.objects.get(id=id)
        basket_obj=request.user.cart
        serializers=BacketItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(product=product_obj,basket=basket_obj)
            return Response(data=serializers.data)
        return Response(data=serializers.errors)
    
class BasketView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def list(self,request,*args, **kwargs):
        qs=request.user.cart 
        serializers=BasketSerializer(qs,many=False)
        return Response(data=serializers.data)

        
        
