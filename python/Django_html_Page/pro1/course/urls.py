from django.urls import path
from . import views

urlpatterns = [
    path('feesdj/',views.learn_django),
    path('feespy/',views.learn_python),
]