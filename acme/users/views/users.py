'''Users Views.'''

# djangorestframework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# serializers
from acme.users.serializers import (UserLoginSerializer,
                                    UserModelSerializer,
                                    UserSignUpSerializer,
                                    UserSignOutSerializer)


class UserLoginAPIView(APIView):
    """User Login Api view"""

    def post(self, request, *args, **kwargs):
        '''Handle Http POST request'''
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """User Signup Api view"""

    def post(self, request, *args, **kwargs):
        """
            Handle Http POST request
        """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignOutAPIView(APIView):
    """User Sign Out Api View"""

    def post(self, request, *args, **kwargs):
        """Handle Http POST request"""
        serializer = UserSignOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'see will you later!'}
        return Response(data, status=status.HTTP_200_OK)
