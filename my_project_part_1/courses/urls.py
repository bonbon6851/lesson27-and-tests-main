from django.urls import path

from courses.views import courses, new_courses, get_course, search

urlpatterns = [
    path('', courses),
    path('new/', new_courses),
    path('search/', search),
    path('<slug>/', get_course)
]
