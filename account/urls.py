from django.urls import path
from django.contrib.auth import views

from .views import login_user, dashboard, logout_view, register, edit


urlpatterns = [
    # предыдущий url входа
    # path('login/', login_user, name='login'),
    # url-адреса входа и выхода
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    # url-адреса смены пароля
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # url-адреса сброса пароля
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #регистрация
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('', dashboard, name='dashboard'),


]