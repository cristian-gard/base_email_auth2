from accounts.views import RegisterView, PasswordChangeView, PasswordChangeDoneView
from . import views
from django.urls import path



urlpatterns = [
    path('login/', views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',
        views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'
        ),
        name='password_reset'),
    path('password_reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    path('password_reset_complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]
