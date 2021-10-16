from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_poems, name='poems'),
    path('<int:poem_id>', views.get_poem_by_id, name='retrieve_poem'),
    path('<int:poem_id>/like', views.like_poem),
    path('<int:poem_id>/dislike', views.dislike_poem),
    path('<int:poem_id>/comment', views.comment_poem, name='comment')
]
