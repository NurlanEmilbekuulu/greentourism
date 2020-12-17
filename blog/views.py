from django.shortcuts import render, get_object_or_404
from .models import Category, Article
from django.db.models import F

def article_list(request, slug=None):
	articles = Article.objects.all()
	categories = Category.objects.all()
	recent_posts = Article.objects.all()[:5]

	if slug:
		category = get_object_or_404(Category, slug=slug)
		articles = Article.objects.filter(category=category)

	return render(request, 'blog/article-list.html', {'article_categories' : categories,'articles' : articles, 'recent_posts' : recent_posts})

def article_detail(request, slug):
	article = get_object_or_404(Article, slug=slug)
	article.view = F('view') + 1
	article.save(update_fields=["view"])
	return render(request, 'blog/article-detail.html', {'article' : article})