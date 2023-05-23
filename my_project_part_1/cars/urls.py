from django.urls import path

from cars.views import get_car, search

urlpatterns = [
    path('search/', search),
    path('<pk>/', get_car)

]
