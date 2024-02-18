from django.urls import path

from .views import PostListViews

urlpatterns = [
    path('list/', PostListViews.as_view())
]
