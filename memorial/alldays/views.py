from django.shortcuts import render
from django.templatetags.static import static
import os

# Create your views here.
def index(request):
    pathname = static("alldays/images/2023/january")
    names = os.listdir('.' + pathname)
    print(names)


    return render(request, "alldays/index.html", {
        "names": names,
        "m": pathname
    })