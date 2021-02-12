from django.shortcuts import render, redirect, get_object_or_404

from website.filters import CarFilter
from cars.forms import CarForm, BuyForm
from cars.models import Car


def list(request):
    # return HttpResponse('List the car')
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            saved = form.save()
            return redirect("thankyou", saved.id)
    else:
        form = CarForm()
    return render(request, "cars/list.html", {"form": form})


def car_search(request):
    f = CarFilter(request.GET, queryset=Car.objects.filter(Make='TOYOTA'))
    context = {'filter': f, }
    return render(request, 'cars/search.html', context)


def buy(request, id):
    car = get_object_or_404(Car, pk=id)
    if request.method == "POST":
        form = BuyForm(request.POST, instance=car)
        if form.is_valid():
            saved = form.save()
            return redirect("confirm", saved.id)
    else:
        form = BuyForm(instance=car)
    return render(request, "cars/buy.html", {"form": form})