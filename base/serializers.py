from rest_framework import serializers
from .models import Product, ProductType, Department, Vendor, Purchase, Sell, User
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from dotenv import load_dotenv
import os
from django.utils.crypto import get_random_string

load_dotenv()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'image', 'groups']

    def create(self, validated_data):
        otp = get_random_string(6, '0123456789')
        user = User.objects.create_user(
            **validated_data, is_active=False, otp=otp)

        send_mail(
            subject="Your otp code",
            message=f"Your otp code is {otp}",
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=[user.email],
        )

        return user


class OtpVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        user = User.objects.filter(
            email=data['email'], otp=data['otp']).first()

        if not user:
            raise serializers.ValidationError("Invalid OTP or email")
        user.is_active = True
        user.otp = None
        user.save()

        return {"message": "User activated successfully"}
