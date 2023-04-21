from django.shortcuts import render , get_object_or_404
from .models import Book

# Create your views here.

def index(request):
    context = {
        "books":Book.objects.filter(published=True),
    }
    return render(request , 'library/index.html', context) 