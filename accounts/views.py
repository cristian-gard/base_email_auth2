from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm

#no login required
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

#login required
class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    template_name = 'accounts/logout.html'

class PasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/password_change_form.html'    
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

class PasswordResetView(LoginRequiredMixin, auth_views.PasswordResetView):
    template_name='accounts/password_reset.html'

class PasswordResetDoneView(LoginRequiredMixin, auth_views.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class PasswordResetConfirmView(LoginRequiredMixin, auth_views.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
   
class PasswordResetCompleteView(LoginRequiredMixin, auth_views.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'  
   