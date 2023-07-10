"""rka3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from course import views as cv
from fees import views as fv
        #   or
# from course import learn_django
# from fees import fees_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learnco/',cv.learn_django),
    path('learnfess/',fv.fees_django),
                # or
    # path('learnco/',learn_django),
    # path('learnfess/',fees_django),
]
