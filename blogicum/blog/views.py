from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.db.models import Q
from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'

    post_list = Post.objects.filter(
        Q(is_published=True)
        & Q(pub_date__lte=now())
        & Q(category__is_published=True)
    ).order_by('-pub_date')[:5]

    content = {'post_list': post_list}

    return render(request, template, content)


def post_detail(request, pk):
    template = 'blog/detail.html'

    post = get_object_or_404(
        Post,
        pk=pk,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )

    content = {'post': post}

    return render(request, template, content)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)

    post_list = Post.objects.filter(
        Q(is_published=True)
        & Q(category=category)
        & Q(pub_date__lte=now())
    ).order_by('-pub_date')

    content = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template, content)
