from django.shortcuts import render, redirect
from .models import Text, Profile
from .forms import RegistrationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'auth/login.html', {'error': 'womp womp, wrong credentials buddy'})
    return render(request, 'auth/login.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Welcome {}'.format(user.username))
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})

def sign_out(request):
    logout(request)
    redirect('index')
@login_required(login_url='/login')
def index(request):
    user = request.user
    if not user.is_superuser:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'index.html', {'user': user, 'profile': profile})
    else:
        return render(request, 'index.html', {'user': request.user})
@login_required(login_url='/login')
def profile(request):
    user = request.user
    if not user.is_superuser:
        form = ProfileForm(instance=request.user.profile)
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            profile.bio = request.POST.get('bio')
            profile.save()
        return render(request, 'profile.html', {'user': user, 'profile': profile, 'form': form})
    else:
        return render(request, 'profile.html', {'user': user,})
@login_required(login_url='/login')
def messager(request):
    texts = Text.objects.all()
    return render(request, 'messager.html', {'texts': texts})
    # return render(request, 'messager.html')
@login_required(login_url='/login')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
