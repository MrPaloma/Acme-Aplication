'''Users Serializers'''

# python
from datetime import timedelta
import jwt

# Django
from django.contrib.auth import authenticate, password_validation

# djangorestframework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# django
from django.core.validators import RegexValidator

# models
from acme.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


class UserLoginSerializer(serializers.Serializer):
    """
    User Login Serializer.
    Handle the login request
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=0, max_length=64)

    def validate(self, data):
        """
        Check credentials.
        """

        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        self.context['user'] = user
        return data

    def create(self, data):
        """
        Generate o Retrieve new token
        """
        token, user = Token.objects.get_or_create(user=self.context['user'])
        return user, token.key


class UserSignUpSerializer(serializers.Serializer):
    """
    User Signup serializer
    Register a new user
    """
    email = serializers.EmailField()
    username = serializers.CharField(min_length=0,
                                     max_length=64,
                                     validators=[UniqueValidator(queryset=User.objects.all())]
                                     )

    # name
    first_name = serializers.CharField(min_length=2, max_length=64)
    last_name = serializers.CharField(min_length=2, max_length=64)

    # password
    password = serializers.CharField(min_length=0, max_length=64)
    password_confirmation = serializers.CharField(min_length=0, max_length=64)

    # phone_number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be between 1 and 15 characters long '
    )
    phone_number = serializers.CharField(min_length=9,
                                         max_length=17,
                                         validators=[phone_regex])

    def validate(self, data):
        """Check data."""

        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:

            error = {
                "password_confirmation": [
                    "Passwords don't match."
                ]
            }

            raise serializers.ValidationError(error)

        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        return user


class UserSignOutSerializer(serializers.Serializer):

    def create(self, data):
        """
        Generate o Retrieve new token
        """
        Token.objects.filter(user=self.context['request'].user).delete()
        return True
