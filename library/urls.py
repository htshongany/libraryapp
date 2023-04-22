from django.urls import path

from .views import index , get_pdf_detail , get_pdf_preview

app_name = 'library'

urlpatterns = [
    path('', index , name='index'),
    path('detail/<str:slug>', get_pdf_detail , name='book-detail'),
    path('preview/<str:slug>', get_pdf_preview , name='book-preview'),
]