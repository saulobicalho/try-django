from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    my_title = "Hello there...."
    return render(request,"hello_world.html",{"title": my_title})

def about_page(request):
    my_title = "More about us...."
    return render(request,"hello_world.html",{"title": my_title})

def contact_page(request):
    my_title = "Please contact us...."
    return render(request,"hello_world.html",{"title": my_title})
