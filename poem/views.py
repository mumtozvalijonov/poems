from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Poem


@login_required(login_url='/accounts/login')
def get_all_poems(request):
    poems = Poem.objects.all()
    return render(request, 'poem/poems.html', context={'poems': poems})


@login_required(login_url='/accounts/login')
def get_poem_by_id(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        return render(request, 'poem/poem.html', context={'poem': poem})
    return render(request, '404.html')