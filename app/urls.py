from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from django.views.generic import RedirectView

from . import views

app_name = 'books'
urlpatterns = [
    path('', RedirectView.as_view(url='/books/')),
    path('books/', views.book_list, name='index'),
    path('books/<int:book_id>/', views.book_info, name='info'),

    path('authors/<int:author_id>/', views.author_info, name='author_info'),

]
