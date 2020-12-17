from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, SubscribeForm
from .models import Tour, Hotel, Service, Offer, Slide,Comment, Category
from blog.models import Article
from django.db.models import F, Q
from django.contrib import messages


def index(request):
	offer = Offer.objects.first()
	recent_posts = Article.objects.all()[:3]
	slides = Slide.objects.all()
	services = Service.objects.all()
	tours = Tour.objects.all()[:8]
	recommended_hotels = Hotel.objects.all()
	popular_tours_f = Tour.objects.all()[:4]
	popular_tours_l = Tour.objects.all()[4:8]
	return render(request, 'index/index.html', 
		{'offer' : offer,
		 'recent_posts' : recent_posts,
		 'slides' : slides,
		 'services' : services,
		 'tours' : tours,
		 'recommended_hotels' : recommended_hotels,
		 'popular_tours_f' : popular_tours_f,
		 'popular_tours_l' : popular_tours_l
		 })

def about(request):
	return render(request, 'index/about.html')

def hotels(request):
	hotels = Hotel.objects.all()
	return render(request, 'index/hotels.html', {'hotels' : hotels})

def hotel_detail(request, slug):
	hotel = get_object_or_404(Hotel, slug=slug)
	hotel.view = F('view') + 1
	hotel.save()
	return render(request, 'index/hotel-room.html', {'hotel' : hotel})

def tours(request, slug=None):
	tours = Tour.objects.all()

	if slug:
		category = get_object_or_404(Category, slug=slug)
		tours = Tour.objects.filter(category=category)

	return render(request, 'index/tours.html', {'tours' : tours})

def tour_detail(request, slug):
	tour = get_object_or_404(Tour, slug=slug)
	tour.view = F('view') + 1
	tour.save()
	return render(request, 'index/tour-place.html', {'tour' : tour})

def services(request):
	services = Service.objects.all()
	return render(request, 'index/services.html', {'services' : services})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			fname = form.cleaned_data['fname']
			lname = form.cleaned_data['lname']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

			full_message = fname + ' ' + lname + '\n' + email + '\n' + message
			try:
				send_mail(subject, full_message, email, ['greentourism07@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
	return render(request, "index/contact.html")

def subscribe(request):
	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('/')


def search_tour(request):
	if request.method == 'GET':
		question = request.GET.get('q')
		if question is not None:
			tours = Tour.objects.filter(Q(name__search=question) | Q(place__search=question))
			return render(request, 'index/tours.html', {'tours' : tours})
	return redirect('/')

def search_hotel(request):
	if request.method == 'GET':
		question = request.GET.get('q')
		if question is not None:
			hotel = Hotel.objects.filter(Q(name__search=question) | Q(place__search=question) | Q(summary__search=question) )
			return render(request, 'index/hotels.html', {'hotels' : hotels})
	return redirect('/')