from django.urls import path
from .views import greenhouse_home


urlpatterns = [
    path('', greenhouse_home, name='greenhouse-home')
]