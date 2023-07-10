from django.urls import path
from . import views

urlpatterns = [
    path('learndj/',views.fees_django),
    path('learnpy/',views.fees_python),
]