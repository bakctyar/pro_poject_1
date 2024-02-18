from django import template

from post.models import Post


register = template.Library()


@register.simple_tag
def latest_posts(count=2):
    return Post.objects.order_by('-publish')[:count]

