from django.db import models
from index.models import Tour

class Social(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	icon = models.CharField(max_length=255, verbose_name='Иконка')
	url = models.URLField(verbose_name='URL путь')

	class Meta:
		verbose_name = 'Социальная сеть'
		verbose_name_plural = 'Социальные сети'

	def __str__(self):
		return self.name

class Contact(models.Model):
	site = models.URLField(verbose_name='Название сайта')
	email = models.EmailField(verbose_name='Электронная почта')
	phone = models.CharField(max_length=255, verbose_name='Телефонный номер')
	address = models.CharField(max_length=500, verbose_name='Адрес')
	location = models.URLField(max_length=500,verbose_name='Локация', null=True)

	class Meta:
		verbose_name = 'Контакт'
		verbose_name_plural = 'Контакты'

	def __str__(self):
		return self.email


class Partner(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	url = models.URLField(verbose_name='URL путь')

	class Meta:
		verbose_name = 'Партнер'
		verbose_name_plural = 'Партнеры'

	def __str__(self):
		return self.name


class Deal(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')

	class Meta:
		verbose_name = 'Предложение'
		verbose_name_plural = 'Предложения'

	def __str__(self):
		return self.name

class Hotlink(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	url = models.URLField(verbose_name='URL путь')

	class Meta:
		verbose_name = 'Актуальное'
		verbose_name_plural = 'Актуальное'

	def __str__(self):
		return self.name