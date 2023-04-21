from django.urls import path

from .views import index , get_pdf_detail

app_name = 'library'

urlpatterns = [
    path('', index , name='index'),
    path('detail/<str:slug>', get_pdf_detail , name='book-detail'),
]