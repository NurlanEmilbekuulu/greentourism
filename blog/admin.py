from django.contrib import admin
from .models import Article, Subscriber, Category

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug' : ('name',)}

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug' : ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Subscriber)