from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User

from publication.serializers import PublicationSerializer


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'password', 'username', 'avatar',
            'phone_number', 'site', 'bio',
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                'wrong credentials', code='auth'
            )

        attrs['user'] = user
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    posts = PublicationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'posts'
        )
        extra_kwargs = {
            'password': {
                'required': False,
                'write_only': True
            },
            'email': {
                'required': False
            },
            'username': {
                'required': False
            }
        }