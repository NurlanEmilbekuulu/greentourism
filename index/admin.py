from django.contrib import admin
from .models import Tour, Hotel, Room, Service, Slide, Tourday, Comment, Offer, Category


class TourdayInline(admin.StackedInline):
	model = Tourday
	extra = 1

class RoomInline(admin.StackedInline):
	model = Room
	extra = 1
	prepopulated_fields = { 'slug' : ('name',)}

class TourAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug' : ('name',)}
	inlines = [TourdayInline,]

class HotelAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug' : ('name',)}
	inlines = [RoomInline,]

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Tour, TourAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Service)
admin.site.register(Slide)
admin.site.register(Comment)
admin.site.register(Offer)
admin.site.register(Category, CategoryAdmin)