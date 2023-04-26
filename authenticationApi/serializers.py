from rest_framework import serializers
from . models import AuthUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model = AuthUser
        fields = ["email", "user_name",  "password", "password2"]
        extra_kwargs = {
            "password":{"write_only":True}
        }
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("both password are not equal!")
        # return super().validate(attrs)
        return attrs
    def create(self, validated_data):
        return AuthUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = AuthUser
        fields = ["email", "password"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["id", "email", "password"]

