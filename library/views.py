from django.shortcuts import render , get_object_or_404
from .models import Book

# Create your views here.

def index(request):
    context = {
        "books":Book.objects.filter(published=True),
    }
    return render(request , 'library/index.html', context)


def get_pdf_detail(request, slug):
    context = {
        "book": get_object_or_404(Book.objects.filter(published=True, slug=slug))
    }

    return render(request,"library/book-view.html" ,context)

def get_pdf_preview(request, slug):
    context = {
        "book": get_object_or_404(Book.objects.filter(published=True, slug=slug))
    }
    return render(request,"library/book-preview.html" ,context)




def search_by_title(request):
    object_list = _search_book(request)
    context = {
        'object_list':object_list,
        }
    
    return render(request,"library/search-results.html" ,context)

def _search_book(request):
    if request.method == "POST":
        # print(request.method.POST['search'])
        search = request.POST.get("search")
        object_list = Book.objects.filter(title__contains=search , published=True)
    return object_list