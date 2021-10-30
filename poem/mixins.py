from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPermissionMixin(LoginRequiredMixin):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'