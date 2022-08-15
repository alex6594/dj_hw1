from django.shortcuts import render

from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'object_list': Article.objects.order_by(ordering).all()}
    print(context)


    return render(request, template, context)
