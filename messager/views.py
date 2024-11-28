from django.shortcuts import render
from .models import Text
from django.shortcuts import redirect
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration.html', {'form': form})

@login_required
def index(request):
    texts = Text.objects.all()
    return render(request, 'index.html', {'texts': texts, 'user': request.user})

# Create your views here.
