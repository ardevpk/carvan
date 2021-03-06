


from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('change-password/', PasswordChange.as_view(), name='change-password'),
    path('reset-password/', PasswordReset.as_view(), name='reset-password'),
    path('reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),

    # path('userChange/', Profile.as_view(), name='userChange'),
]
