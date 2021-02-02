from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, AllUsers, GetRecentUsers
from knox import views as knox_views

urlpatterns = [
    path('api/', include('knox.urls')),
    path('api/register', RegisterAPI.as_view()),
    path('api/login', LoginAPI.as_view()),
    path('api/user', UserAPI.as_view()),
    path('api/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/users/', AllUsers.as_view()),
    path('api/lastusers/', GetRecentUsers.as_view(), )
]
