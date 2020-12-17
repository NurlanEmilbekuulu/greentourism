from django.template.context_processors import request
from index.forms import SubscribeForm, BookingTourForm, BookingRoomForm, ContactForm
from index.models import Comment, Category
from sitesettings.models import Social, Contact, Partner, Deal, Hotlink

def index(request):
	contact_form = ContactForm()
	subscribe_form = SubscribeForm()
	booking_tour_form = BookingTourForm()
	booking_room_form = BookingRoomForm()

	comments = Comment.objects.all()
	socials = Social.objects.all()
	contact = Contact.objects.first()
	partners = Partner.objects.all()
	deals = Deal.objects.all()
	hotlinks = Hotlink.objects.all()

	categories = Category.objects.all()

	return {
		'contact_form' : contact_form,
		'subscribe_form' : subscribe_form,
		'booking_tour_form' : booking_tour_form,
		'booking_room_form' : booking_room_form,

		'comments' : comments,
		'socials' : socials,
		'contact' : contact,
		'partners' : partners,
		'deals' : deals,
		'hotlinks' : hotlinks,

		'categories' : categories
	}