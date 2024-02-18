from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.contrib.postgres.search import TrigramSimilarity

from .models import Post, Comment
from .forms import CommentForm, EmailPostForm, SearchForm

def post_list(request, tag_slug=None):
    post_list = Post.objects.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'post/index.html', {'posts': posts, 'tag': tag})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    comments = post.comments.filter(active=True)

    form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, template_name='post/detail.html', context={'post': post,
                                                                      'comments': comments,
                                                                      'form': form,
                                                                      'similar_posts': similar_posts})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = None
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

    return render(request, 'post/comment.html', {'post': post, 'form': form, 'comment': comment})




def search_post(request):
    form = SearchForm()
    query = None
    results = []
    search_get = 0

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        search_get = request.GET
        if form.is_valid():
            query = form.cleaned_data['query']
            # results = Post.objects.annotate(
            #     similarity=TrigramSimilarity('title', query)
            # ).filter(similarity__gt=0.1).order_by('-similarity')

            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')



    return render(request, 'post/search.html', {'form': form, 'query': query, 'results': results,'search_get': search_get})


















# def send_email(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     send = False
#     if request.method == 'POST':
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             sd = form.cleaned_data
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = ''



