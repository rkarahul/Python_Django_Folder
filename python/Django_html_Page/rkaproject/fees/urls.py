from django.urls import path
from . import views

urlpatterns = [
   path('learndj/',views.fees_django),
   path('learnfs/',views.fees_python),
]