from django.shortcuts import render
from django.http import HttpResponse
from portfillo.models import contact

# Create your views here.
def home(request):
    return render(request , "index.html" )


def form(request):
    if request.method == "POST":
        # print(request.POST)
        name = request.POST.get("name" , "unknown")
        email = request.POST.get("email" , "empty")

        # print(name, email)
        contact.objects.create(
            name = name,
            email = email 
        )


    return render(request , "form.html")
