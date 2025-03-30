from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = [
            'id',
            'role',
            'first_name',
            'last_name',
            'username',
            'age',
            'location',
            'password',
        ]
        # ¿MAYOR TIEMPO EN REQUEST?
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            'gender': {'required': True},
            'age': {'required': True},
            'location': {'required': True},
        }
        
    def create(self, validated_data):
        # Hash de contraseña antes de guardar
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
    
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError('You must be at least 18 years old.')
        return value
        
class PropertySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Property
        fields = '__all__'
        
class RentalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalHistory
        fields = '__all__'