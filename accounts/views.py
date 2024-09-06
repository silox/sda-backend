from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, TemplateView

from viewer.forms import CustomAuthenticationForm, CustomPasswordChangeForm, SignUpForm


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(), 'object': self.request.user}

    def test_func(self):
        return timezone.now() - timedelta(days=7) > self.request.user.date_joined


class SubmittableLoginView(LoginView):
    template_name = 'login_form.html'
    form_class = CustomAuthenticationForm
    next_page = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('index')
    form_class = CustomPasswordChangeForm


class SignUpView(CreateView):
    template_name = 'sign_up_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')
