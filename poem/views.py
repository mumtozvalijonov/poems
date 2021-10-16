from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

from poem.forms import CommentForm

from .models import Poem


@login_required(login_url='/accounts/login')
def get_all_poems(request):
    poems = Poem.objects.all()
    return render(request, 'poem/poems.html', context={'poems': poems})


@login_required(login_url='/accounts/login')
def get_poem_by_id(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        return render(request, 'poem/poem.html', context={'poem': poem, 'comment_form': CommentForm()})
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

@login_required(login_url='/accounts/login')
def comment_poem(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            poem.comment_set.create(user=request.user, text=form.cleaned_data['comment'])
            return redirect('retrieve_poem', poem_id=poem_id)
    return render(request, '404.html')
