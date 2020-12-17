from django.contrib import admin
from .models import BookingTour, BookingRoom

class BookingTourAdmin(admin.ModelAdmin):
	list_display = ('person','tour', 'check_in', 'check_out', 'adults', 'children', 'date') 

class BookingRoomAdmin(admin.ModelAdmin):
	list_display = ('person','room', 'check_in', 'check_out', 'rooms', 'adults', 'children', 'date')


admin.site.register(BookingTour, BookingTourAdmin)
admin.site.register(BookingRoom, BookingRoomAdmin)