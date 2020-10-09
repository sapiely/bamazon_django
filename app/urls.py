from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register("books", views.BookViewSet)
router.register("authors", views.AuthorViewSet)

app_name = "books"
urlpatterns = [
    path("api/", include(router.urls)),
    path("", RedirectView.as_view(url="/books/")),
    path("books/", views.book_list, name="books"),
    path("books/<int:book_id>/", views.book_info, name="book_info"),
    path("authors/", views.author_list, name="authors"),
    path("authors/<int:author_id>/", views.author_info, name="author_info"),
]
