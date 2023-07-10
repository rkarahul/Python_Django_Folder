from django.urls import path
from . import views

urlpatterns = [
    path('learnc/',views.course_django),
    path('learnf/',views.fees_django),
]