from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from .models import Poem, Like


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


@login_required(login_url='/accounts/login')
def like_poem(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        try:
            poem.like_set.create(user=request.user)
        except IntegrityError:
            return HttpResponse('This poem is already liked')
        return HttpResponse('Liked successfully')
    return render(request, '404.html')


@login_required(login_url='/accounts/login')
def dislike_poem(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        try:
            poem.dislike_set.create(user=request.user)
        except IntegrityError:
            return HttpResponse('This poem is already disliked')
        return HttpResponse('Disliked successfully')
    return render(request, '404.html')
