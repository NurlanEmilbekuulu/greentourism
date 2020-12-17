from django.db import models
from django.contrib.auth.models import User
from index.models import Tour, Room

class BookingTour(models.Model):
	person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
	date = models.DateField(auto_now=True, verbose_name='Время бронирования')
	check_in = models.DateField(verbose_name='Заезд')
	check_out = models.DateField(verbose_name='Отъезд')
	adults = models.PositiveIntegerField(verbose_name='Количество взрослых')
	children = models.PositiveIntegerField(verbose_name='Количество детей')

	class Meta:
		verbose_name='Бронирование Тура'
		verbose_name_plural='Бронирование Туров'

	def __str__(self):
		return self.person.username

class BookingRoom(models.Model):
	person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
	room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната')
	date = models.DateField(auto_now=True, verbose_name='Время бронирования')
	check_in = models.DateField(verbose_name='Заезд')
	check_out = models.DateField(verbose_name='Отъезд')
	rooms = models.PositiveIntegerField(verbose_name='Количество комнат')
	adults = models.PositiveIntegerField(verbose_name='Количество взрослых')
	children = models.PositiveIntegerField(verbose_name='Количество взрослых')


	class Meta:
		verbose_name='Бронирование Комнаты'
		verbose_name_plural='Бронирование Комнат'

	def __str__(self):
		return self.person.username