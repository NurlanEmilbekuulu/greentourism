from django.shortcuts import render, redirect, get_object_or_404
from index.forms import BookingTourForm, BookingRoomForm
from django.http import HttpResponse, HttpResponseRedirect
from index.models import Tour, Room
from django.contrib.auth.decorators import login_required

@login_required
def book_tour(request, slug):
	tour = get_object_or_404(Tour, slug=slug)
	if request.method == 'POST':
		form = BookingTourForm(request.POST)
		if form.is_valid():
			booking_tour = form.save(commit=False)
			booking_tour.person = request.user
			booking_tour.tour = tour
			booking_tour.save()
			return redirect('index:index')
	return render(request, 'book/book-tour.html', {'tour' : tour})

@login_required
def book_room(request, slug):
	room = get_object_or_404(Room, slug=slug)
	if request.method == 'POST':
		form = BookingRoomForm(request.POST)
		if form.is_valid():
			booking_room = form.save(commit=False)
			booking_room.person = request.user
			booking_room.room = room
			booking_room.save()
			return redirect('index:index')
	return render(request, 'book/book-room.html', {'room' : room})