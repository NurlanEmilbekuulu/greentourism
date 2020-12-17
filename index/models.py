from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField

ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5

RATING = (
	(ONE, '1 звезда'),
	(TWO, '2 звезды'),
	(THREE, '3 звезды'),
	(FOUR, '4 звезды'),
	(FIVE, '5 звезд'),
)

class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	slug = models.SlugField(max_length=255, verbose_name='Строка')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('index:tours_by_category', args=[self.slug])

# Model Tour 
class Tour(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
	name = models.CharField(max_length=255, verbose_name='Название')
	slug = models.SlugField(max_length=255, verbose_name='Строка')
	image = models.ImageField(upload_to="tour/image/%Y/%m/%d/", verbose_name='Картинка')
	description1 = RichTextUploadingField(null=True, blank=True)
	description2 = RichTextUploadingField(null=True, blank=True)
	image_3d = models.URLField(verbose_name='3D изображение', null=True, blank=True)
	place = models.CharField(max_length=255, verbose_name='Расположение')
	price = models.PositiveIntegerField(verbose_name='Цена')
	rating = models.PositiveIntegerField(choices=RATING, default=ONE, verbose_name='Рейтинг')
	view = models.PositiveIntegerField(null=True, default=0, verbose_name='Количество просмотров')

	class Meta:
		verbose_name='Тур'
		verbose_name_plural='Туры'

	def __str__(self):
		return self.name

	def book(self):
		return reverse('book:book_tour', args=[self.slug])

	def get_absolute_url(self):
		return reverse('index:tour_detail', args=[self.slug])


# Model Hotel

class Hotel(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	slug = models.SlugField(max_length=255, verbose_name='Строка')
	image = models.ImageField(upload_to="hotel/image/%Y/%m/%d/", verbose_name='Картинка')
	place = models.CharField(max_length=255, verbose_name='Расположение')
	price = models.PositiveIntegerField(verbose_name='Цена')
	rating = models.PositiveIntegerField(choices=RATING, default=ONE, verbose_name='Рейтинг')
	summary = models.TextField(null=True, verbose_name='Краткое описание')
	view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

	class Meta:
		verbose_name='Гостиница'
		verbose_name_plural='Гостиницы'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('index:hotel_detail', args=[self.slug])

# Model Room
class Room(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Гостиница')
	name = models.CharField(max_length=255, verbose_name='Название')
	slug = models.SlugField(max_length=255, verbose_name='Строка')
	image = models.ImageField(upload_to="room/image/%Y/%m/%d/", null=True, verbose_name='Картинка')
	price = models.PositiveIntegerField(verbose_name='Цена')
	description = models.TextField(verbose_name='Краткое описание')

	class Meta:
		verbose_name='Комната'
		verbose_name_plural='Комнаты'

	def __str__(self):
		return self.name

	def book(self):
		return reverse('book:book_room', args=[self.slug])

# Model Service
class Service(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название')
	icon = models.CharField(max_length=255, verbose_name='Иконка')
	description = models.TextField(verbose_name='Описание')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Услуга'
		verbose_name_plural='Услуги'

# Model Slide

class Slide(models.Model):
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')
	image = models.ImageField(upload_to="slide/image/%Y/%m/%d/", verbose_name='Картинка')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Слайд'
		verbose_name_plural='Слайды'


class Tourday(models.Model):
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, verbose_name='Тур')
	day = models.PositiveIntegerField(default=0, verbose_name='День')
	name = models.CharField(max_length=100, verbose_name='Название')
	preview = models.ImageField(upload_to="tourday/preview/%Y/%m/%d/", verbose_name='Картинка')
	description = models.TextField(verbose_name='Описание')

	class Meta:
		ordering=['id']
		verbose_name='Программа дня'
		verbose_name_plural='Программа дней'

	def __str__(self):
		return str(self.day)


class Comment(models.Model):
	author = models.CharField(max_length=255, verbose_name='Автор')
	image = models.ImageField(upload_to="comment/image/%Y/%m/%d/", verbose_name='Картинка')
	country = models.CharField(max_length=255, verbose_name='Страна')
	text = models.TextField(verbose_name='Текст')

	class Meta:
		verbose_name='Отзыв'
		verbose_name_plural='Отзывы'

	def __str__(self):
		return self.author

class Offer(models.Model):
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
	sale = models.PositiveIntegerField(verbose_name='Скидка')
	text = models.TextField(verbose_name='Текст')

	class Meta:
		verbose_name='Акция'
		verbose_name_plural='Акции'

	def __str__(self):
		return self.tour.name