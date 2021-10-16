from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.log_user_in, name='login'),
    path('register/', views.register, name='register'),
    path('activate/<int:uid>/<str:token>', views.activate, name='activate')
]
