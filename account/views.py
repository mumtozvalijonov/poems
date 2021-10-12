from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login


def log_user_in(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next') or '/poems/'
        return redirect(next_url)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', context={'form': form, 'next': request.GET.get('next') or '/poems/'})


def register(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next') or '/poems/'
        return redirect(next_url)
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url)
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', context={'form': form, 'next': request.GET.get('next') or '/poems/'})
