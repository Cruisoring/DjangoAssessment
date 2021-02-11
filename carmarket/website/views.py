from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from cars.models import Car

CARS_PER_PAGE = 10

def home(request, page_no=0):
    start = page_no*10
    return HomeListView.as_view(
        queryset=Car.objects.order_by("-id")[start:start+10],  # :10 limits the results to the then most recent
        context_object_name="car_list",
        template_name="website/home.html",
    )

class HomeListView(ListView):
    """Renders the home page, with maximum 10 cars."""
    model = Car
    template_name = "website/home.html"
    context_object_name="car_list"
    paginate_by = 10 

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['make'] = self.request.GET.get('make', 'Toyota')
        context['orderby'] = self.request.GET.get('orderby', '-Year')
        return context

    # def get_queryset(self, **kwargs):
    #     make = self.request.GET.get('make', 'None')
    #     year = self.request.GET.get('year', 'None')
    #     order = self.request.GET.get('orderby', '-Year')
    #     q = Car.objects if make == 'None' else Car.objects.filter(Make=make,)
    #     q = q if make == 'None' else q.filter(Year = year,)
    #     q = q.order_by(order)
    #     return q


class SelectView(ListView):
    """Renders the home page, with maximum 10 cars."""
    model = Car
    template_name = "website/home.html"
    context_object_name="car_list"
    paginate_by = 10 

    def get_context_data(self, **kwargs):
        context = super(SelectView, self).get_context_data(**kwargs)
        context['make'] = self.request.GET.get('make', 'Toyota')
        context['orderby'] = self.request.GET.get('orderby', '-Year')
        return context

    def get_queryset(self, **kwargs):
        make = self.request.GET.get('make', 'None')
        year = self.request.GET.get('year', 'None')
        order = self.request.GET.get('orderby', '-Year')
        q = Car.objects if make == 'None' else Car.objects.filter(Make=make,)
        q = q if make == 'None' else q.filter(Year = year,)
        q = q.order_by(order)
        return q

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def thankyou(request, id):
    return render(request, 'website/thankyou.html', {'id': id})