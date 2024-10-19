# admin_custom/serializers.py
from rest_framework import serializers
from .models import Utilisateur

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [ 'email', 'password', 'user_type','first_name','last_name']

    def create(self, validated_data):
        # Hash the password before saving the user
        user = Utilisateur(
            email=validated_data['email'],
            user_type=validated_data['user_type'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],


        )
        user.set_password(validated_data['password'])
        user.save()
        return user
