from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from cars.models import Car

CARS_PER_PAGE = 10

def home(request, page_no=1):
    all_entries = Car.objects.all()
    # cars = sorted(all, key='id', reverse=True)

    paginator = Paginator(all_entries, CARS_PER_PAGE)
    print(paginator.count)
    print(paginator.page_range)
    
    cars_page = tuple([car for car in paginator.page(page_no).object_list])
    # cars_of_page = current_page.object_list

    return render(request, 'website/home.html', {cars_page: cars_page})

class HomeListView(ListView):
    """Renders the home page, with maximum 10 cars."""
    model = Car

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def thankyou(request, id):
    return render(request, 'website/thankyou.html', {'id': id})