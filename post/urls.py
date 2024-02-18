from django.urls import path


from .views import post_list, post_detail, post_comment, search_post
from .feeds import LatestPostsFeed

app_name = 'post'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('dt/<slug:slug>/', post_detail, name='post_detail'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', search_post, name='post_search'),

]
