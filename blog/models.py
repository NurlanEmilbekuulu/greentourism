from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse

class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	slug = models.SlugField(max_length=255, verbose_name='Строка')

	class Meta:
		verbose_name='Категория'
		verbose_name_plural='Категории'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:article_list_by_category', args=[self.slug])

class Article(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
	author = models.CharField(max_length=255, null=True, default='Admin', verbose_name='Автор')
	title = models.CharField(max_length=255, verbose_name='Заглавие')
	slug = models.SlugField(max_length=255, verbose_name='Строка')
	preview = models.ImageField(upload_to="article/preview/%Y/%m/%d/", verbose_name='Превью')
	published = models.DateField(null=True, verbose_name='Время публикации')
	content = RichTextUploadingField(verbose_name='Контент')
	view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

	class Meta:
		verbose_name='Статья'
		verbose_name_plural='Статьи'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:article_detail', args=[self.slug])



class Subscriber(models.Model):
	email = models.EmailField(verbose_name='Электронная почта')

	class Meta:
		verbose_name='Подписчик'
		verbose_name_plural='Подписчики'

	def __str__(self):
		return self.email
