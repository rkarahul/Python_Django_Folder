from django.urls import path
from . import views

urlpatterns = [
    path('learndj/',views.course_django),
    path('learnpy/',views.course_python),
]