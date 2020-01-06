# polling/urls.py

from django.urls import path
from blogging.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('blogs/<int:blog_id>/', detail_view, name="blog_detail"),
]