from django.contrib import admin
from .models import Accommodation, Booking, roomCount, roomImages

# Custom admin class for Accommodation
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price_per_month')
    list_filter = ('name',)
    search_fields = ('name', 'address', 'description')
    # Customize other admin options as needed

# Custom admin class for Booking
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'accommodation', 'status')
    list_filter = ('status',)
    search_fields = ('student__first_name', 'student__last_name', 'accommodation__name')
    # Customize other admin options as needed

# Custom admin class for roomCount
class RoomCountAdmin(admin.ModelAdmin):
    list_display = ('Accommodation', 'count')
    search_fields = ('Accommodation__name',)
    # Customize other admin options as needed

# Register the models and their custom admin classes
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(roomCount, RoomCountAdmin)
admin.site.register(roomImages)
