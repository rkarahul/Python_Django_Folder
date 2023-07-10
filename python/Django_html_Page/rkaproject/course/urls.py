from django.urls import path
from . import views

urlpatterns = [
   path('coursedj/',views.course_django),
   path('coursepy/',views.course_python),
]