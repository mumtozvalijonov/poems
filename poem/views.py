from django.shortcuts import render

from .models import Poem


def get_all_poems(request):
    poems = Poem.objects.all()
    return render(request, 'poem/poems.html', context={'poems': poems})


def get_poem_by_id(request, poem_id):
    poem = Poem.objects.filter(id=poem_id).first()
    if poem:
        return render(request, 'poem/poem.html', context={'poem': poem})
    return render(request, '404.html')