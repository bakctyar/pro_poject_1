from rest_framework import generics

from .serializer import PostSerializer
from post.models import Post

class PostListViews(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
