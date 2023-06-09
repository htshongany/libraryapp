from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index , get_pdf_detail , get_pdf_preview , search_by_title , get_pdf_by_category

app_name = 'library'

urlpatterns = [
    path('', index , name='index'),
    path('detail/<str:slug>', get_pdf_detail , name='book-detail'),
    path('preview/<str:slug>', get_pdf_preview , name='book-preview'),
    path('search/results/', search_by_title , name='search-results'),
    path('book/category/<str:cat_slug>', get_pdf_by_category, name='book-category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

