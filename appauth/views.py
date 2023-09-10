from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .models import User
import re
# Create your views here.

# check email_address format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    'VYV$2rz]esI~'
    return re.match(pattern, email) is not None

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            user = User(email=email, first_name=firstname, last_name=lastname, admin=True)
            user.set_password(password)
            user.save()
            return redirect('signin')
    else:
        form = RegisterForm()
    return render(request, 'auths/signup.html', {'form':form})

def signup_api(request):
    email = request.GET.get('user_email')
    if is_valid_email(email):
        query_user = User.objects.filter(email=email)
        if query_user:
            return JsonResponse({'mssg':'Email Taken'})
        else:
            return JsonResponse({'mssg': 'Perfect!'})
    else:
        return JsonResponse({'mssg': 'Checking...'})

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('/')
        else:
            return HttpResponse('An error occured :(')

    context = {}
    return render(request, 'auths/signin.html', context)


def signout(request):
    context = {}
    return render(request, 'auths/signout.html', context)