from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def log_user_in(request):
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
