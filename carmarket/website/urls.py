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

from website.views import home, thankyou, contact, about, HomeListView
from cars.models import Car

home_list_view = HomeListView.as_view(
    queryset=Car.objects.order_by("-id")[:10],  # :10 limits the results to the then most recent
    context_object_name="car_list",
    template_name="website/home.html",
)

urlpatterns = [
    path('', home_list_view, name='home'),
    # path(r'^(?P<page_no>\w+)/$', home),
    path('thankyou/<int:id>', thankyou, name='thankyou'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
]

urlpatterns += staticfiles_urlpatterns()