from django.shortcuts import render

from drones.models import Drone


def home_page(request):
    drones = Drone.objects.filter(is_published=True)
    return render(request, "homepage/index.html", {"drones": drones})
