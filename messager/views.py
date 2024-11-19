from django.shortcuts import render
from .models import Text
def index(request):
    texts = Text.objects.all()
    return render(request, 'index.html', {'texts': texts})

# Create your views here.
