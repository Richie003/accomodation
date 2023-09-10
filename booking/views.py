from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index/index.html', context)

def Accomodation_listing(request):
    query_accomodation = Accommodation.objects.all()
    context = {
        'dataset':query_accomodation
    }
    return render(request, 'index/rooms.html', context)

def accomodation_detail(request, pk):
    query_accomodation = Accommodation.objects.get(id=pk)
    context = {
        'data':query_accomodation
    }
    return render(request, 'index/room-details.html', context)

def processBooking(request):
    if request.method == 'POST':
        objID = request.POST.get('ID')
        try:
            check_count = roomCount.objects.get(Accommodation_id=objID)
            print(type(check_count.count))
            if check_count.count <= 0:
                return JsonResponse({'negative':f'There are no spaces in {check_count.Accommodation.name}'})
            elif check_count.count > 0:
                Booking.objects.create(
                    student_id = request.user.id,
                    accommodation_id=objID,
                    status=True
                )
                check_count.count = check_count.count - 1
                check_count.save()
                return JsonResponse({
                    'positive':'Booked successfully!'
                }, safe=False)
        except:
            return JsonResponse({'server_err':'An error occured'})

def about(request):
    context = {}
    return render(request, 'index/about-us.html', context)