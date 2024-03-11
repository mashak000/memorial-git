from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.templatetags.static import static
import os
from .services import get_all_rows
import time
from .models import Year23
import json
from django.core import serializers






# index
def index(request):
    pathname = static("alldays/images/2023/high")
    low = static("alldays/images/2023/low")
    names = os.listdir('./alldays'+low)

    return render(request, "alldays/index.html", {
        "names": names,
        "highquality": pathname,
        "low": low,
       
        
    })

# this variant is based on the google API and it is really slow (2-3s to fetch) so it goes only with preloader 
def tables(request, name):
    days = get_all_rows("January 2023")
    newday = ''
    for day in days:
        if day['filename'] == name:
            newday = day
    return JsonResponse(newday, safe=False)

# with django models
def tablesdb(request, name):
    newday = list(Year23.objects.filter(filename=name)) #need error checking
    print(newday)
    day = serializers.serialize('json', newday)
    return JsonResponse(day, safe=False)

    
