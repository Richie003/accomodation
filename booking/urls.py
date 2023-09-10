from django.urls import path
from booking import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
    path('hostels/', views.Accomodation_listing, name='accoms'),
    path('hostel-detail/<int:pk>/view/', views.accomodation_detail, name='accom_details'),
    path('process-booking/', views.processBooking, name='processBooking'),
    path('about/', views.about, name='about')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)