from django.urls import path

from .views import index

app_name = 'library'

urlpatterns = [
    path('', index , name='index')
]