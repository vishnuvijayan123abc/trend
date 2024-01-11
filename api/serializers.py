from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Product,Basket,BasketItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)   
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__" 
        read_only_fields=["id","category"] 
    category=serializers.StringRelatedField()      

class BacketItemSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    class Meta:
        model=BasketItem
        fields="__all__" 
        read_only_fields=["id",
                          "basket",
                          "product",
                          "is_active",
                          "created_at",
                          "updated_at",
                          "total"
                          ]   
        
class BasketSerializer(serializers.ModelSerializer):
    cart_item=BacketItemSerializer(read_only=True,many=True)
    owner=serializers.StringRelatedField()
    class Meta:
        model=Basket  
        fields="__all__"
        read_only_fields=["id",
                          "owner",
                          "is_active",
                          "created_at",
                          "updated_at",
                          "cart_item"
                          ]