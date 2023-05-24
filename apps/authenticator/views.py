from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):

    if request.user.is_authenticated:
        return HttpResponse("Logged IN")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html')
def next(request):
    return redirect(reverse('home'))