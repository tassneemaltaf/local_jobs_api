from rest_framework import serializers
from .models import Job, CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'role', 'profile_picture', 'password', 'password2']
        extra_kwargs = {
                'email': {'required': True},
                'role': {'required': True}
        }

    def validate(self, data):
        """
        Check if the passwords match.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return data
    
    def create(self, validated_data):
        """
        Create and return a new user instance, with hashed password.
        """
        validated_data.pop('password2', None)
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'job_title', 'location', 'job_description']
        read_only_fields = ['recruiter']