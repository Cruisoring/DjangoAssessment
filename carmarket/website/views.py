from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
import numbers

from cars.forms import ConfirmForm
from cars.models import Car, Customer
from website.filters import CarFilter

CARS_PER_PAGE = 10


def home(request):
    context = {}
    order = request.GET.get('order', None)
    if order:
        context['order'] = order
    asc = 'asc' in request.GET and request.GET.get('asc')
    if asc:
        context['asc'] = asc

    make = request.GET.get('Make', None)
    year = request.GET.get('Year', None)

    cars = Car.objects.all()
    if make and make != '':
        print(type(make))
        cars = cars.filter(Make=make)
        context['Make'] = make

    if year and year != '':
        print(type(year))
        year = int(year)
        cars = cars.filter(Year=year)
        context['Year'] = year

    order = order or 'Year'
    cars = cars.order_by(order if asc else '-' + order)

    paginator = Paginator(cars, 10)

    f = CarFilter(request.GET, queryset=cars)

    page_number = request.GET.get('page', 1)
    context['page'] = page_number
    context_str = '&'.join([f'{k}={v}' for k, v in context.items()])
    page_obj = paginator.get_page(page_number)

    return render(request, 'website/home.html', {
        'filter': f,
        'page_obj': page_obj,
        'range': paginator.page_range,
        'order': order,
        'asc': asc,
        'context': context_str
    })


class HomeListView(ListView):
    """Renders the home page, with maximum 10 cars."""
    model = Car
    template_name = "website/home.html"
    context_object_name = "car_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['make'] = self.request.GET.get('make', 'Toyota')
        context['orderby'] = self.request.GET.get('orderby', '-Year')
        return context


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = Customer.objects.all();

        try:
            m = users.get(username=username)
            if m.password == password:
                request.session['member_username'] = m.username
                return HttpResponse("You're logged in.")
        except:
            comment = None
        return HttpResponse("Your username and password didn't match.")
    else:
        return render(request, 'website/login.html')


def logout(request):
    auth.logout(request) 
    return redirect(home)


def about(request):
    return render(request, "website/about.html")


def contact(request):
    return render(request, "website/contact.html")


def thankyou(request, id):
    return render(request, 'website/thankyou.html', {'id': id})


def confirm(request, id):
    car = get_object_or_404(Car, pk=id)
    if request.method == "POST":
        form = ConfirmForm(request.POST, instance=car)
        if form.is_valid():
            saved = form.save()
            return redirect("congratulate", saved.id)
    else:
        form = ConfirmForm(instance=car)
    return render(request, "website/confirm.html", {"form": form})


def congratulate(request, id):
    car = get_object_or_404(Car, pk=id)
    if request.method == "POST":
        form = ConfirmForm(request.POST, instance=car)
        if form.is_valid():
            saved = form.save()
            return redirect("thankyou", saved.id)
    else:
        form = ConfirmForm(instance=car)
    return render(request, "website/congratulate.html", {"form": form, 'car': car})
    # return render(request, 'website/congratulate.html', {'id': id})
