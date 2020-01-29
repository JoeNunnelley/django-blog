# blogging/urls.py

from django.urls import include, path
from rest_framework import routers
from blogging.views import list_view, detail_view, UserViewSet
from blogging.views import GroupViewSet, PostViewSet, CategoryViewSet
from blogging.syndication import LatestEntriesFeed

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', list_view, name='blog_root'),
    path('blog', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('latest/feed/', LatestEntriesFeed()),
    path('api', include(router.urls)),
]
