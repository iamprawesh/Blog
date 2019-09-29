from django.urls import path
from . import views

app_name  = 'blog'


urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create_post,name='create'),
    path('<str:slug>/',views.article_detail,name='detail'),
]
