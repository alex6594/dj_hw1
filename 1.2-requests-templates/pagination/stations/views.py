from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings

def index(request):
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    list_reader = list(reader)

def bus_stations(request):

    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(list_reader, 10)
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)