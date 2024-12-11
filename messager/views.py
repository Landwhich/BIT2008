from django.shortcuts import render, redirect
from .models import Text, Room
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'auth/login.html', {'error': 'womp womp, wrong credentials buddy'})
    return render(request, 'auth/login.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration.html', {'form': form})

def sign_out(request):
    logout(request)
    redirect('/')
@login_required(login_url='/login')
def index(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms': rooms, 'user': request.user})
@login_required(login_url='/login')
def messager(request):
    texts = Text.objects.all()
    return render(request, 'messager.html', {'texts': texts, 'user': request.user})
