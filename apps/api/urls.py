from django.urls import path
from .views.auth import ObtainAuthToken, GroupList
from .views.users import UserByOrganizationList, UserDetail

urlpatterns = [
    path('auth/login/', ObtainAuthToken.as_view()),
    path('auth/groups/', GroupList.as_view()),

    path('users/', UserByOrganizationList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
