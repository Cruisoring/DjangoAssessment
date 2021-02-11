"""carmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from website.views import home, thankyou, contact, about, HomeListView, SelectView
from cars.models import Car

def get_home_list(page_no=0):
    start = page_no*10
    return HomeListView.as_view(
        queryset=Car.objects.order_by("-id")[start:start+10],  # :10 limits the results to the then most recent
        # context_object_name="car_list",
        # template_name="website/home.html",
    )

def select_list():
    return SelectView.as_view(
        queryset=Car.objects.order_by("-id")[0:10],  # :10 limits the results to the then most recent
    )

urlpatterns = [
    path('', get_home_list(), name='home'),
    # path('page/<page_no>', HomeListView.as_view()),
    path('thankyou/<int:id>', thankyou, name='thankyou'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('select?filter=<filter_val>&orderby=<order_val>', select_list(), name='select'),
]

urlpatterns += staticfiles_urlpatterns()