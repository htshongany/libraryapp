from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import Book , Category


# Create your views here.

def index(request):
    object_list = Book.objects.filter(published=True)
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page', 1)
    current_page = paginator.get_page(page_number)
    context = {
        'object_list': current_page.object_list,
        'paginator': paginator,
        'page_number': page_number,
        'page_obj':current_page,
    }
    return render(request, 'library/index.html', context)


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

def get_pdf_by_category(request, cat_slug):
    category = get_object_or_404(Category.objects.filter(slug=cat_slug))
    books = Book.objects.filter(category=category, published=True)

    context = {
        'object_list': books,
    }
    return render(request, 'library/book-category.html', context)

def search_by_title(request):
    object_list = _search_book(request)
    context = {
        'object_list':object_list,
        }
    return render(request,"library/search-results.html" ,context)

def _search_book(request):
    object_list = []
    if request.method == "POST":
        search = request.POST.get("search")
        object_list = Book.objects.filter(title__contains=search , published=True)
    return object_list