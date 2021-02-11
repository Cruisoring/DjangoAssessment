from django.http import HttpResponse
from django.shortcuts import render, redirect

from cars.forms import CarForm


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
