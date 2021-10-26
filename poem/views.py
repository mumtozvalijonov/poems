from django.http.response import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.db.models import Q

from poem.forms import CommentForm, PoemForm

from .models import Poem


@login_required(login_url='/accounts/login')
def get_all_poems(request):
    search = request.GET.get('search', '')
    sort_by_author = request.GET.get('sort_by_author', 'asc')
    sort_by_name = request.GET.get('sort_by_name', 'asc')
    sorting = (
        'author__last_name' if sort_by_author == 'asc' else '-author__last_name',
        'name' if sort_by_name == 'asc' else '-name'
    )
    search_filter = []
    if search:
        search_filter.append(
            Q(name__icontains=search) |
            Q(author__first_name__icontains=search) |
            Q(author__last_name__icontains=search)
        )
    poems = Poem.objects.filter(*search_filter).order_by(*sorting)
    return render(
        request,
        'poem/poems.html',
        context={
            'poems': poems,
            'search': search,
            'sort_by_author': sort_by_author,
            'sort_by_name': sort_by_name
        }
    )


@login_required(login_url='/accounts/login')
def get_poem_by_id(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        return render(request, 'poem/poem.html', context={'poem': poem, 'comment_form': CommentForm()})
    return render(request, '404.html')


@login_required(login_url='/accounts/login')
def update_poem_by_id(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if not poem:
        return render(request, '404.html')
    if request.method == 'POST':
        form = PoemForm(data=request.POST, instance=poem)
        if form.is_valid():
            form.save()
            return redirect(reverse('retrieve_poem', kwargs={'poem_id': poem.id}))
    else:
        form = PoemForm()
    return render(request, 'poem/poem_update.html', context={'poem': poem, 'form': form})
    

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
