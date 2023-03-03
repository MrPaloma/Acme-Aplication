"""Users urls"""

# Django
from django.urls import path

# Views
from acme.users.views import (UserLoginAPIView,
                                UserSignUpAPIView,
                                UserSignOutAPIView)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/sign-out/', UserSignOutAPIView.as_view(), name='sign-out')
]
