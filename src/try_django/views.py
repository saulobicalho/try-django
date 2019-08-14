from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    my_title = "Hello there...."
    context = {"title": my_title}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,3,4,5]}
    return render(request,"home.html",context)

def about_page(request):
    my_title = "More about us...."
    return render(request,"about.html",{"title": my_title})

def contact_page(request):
    my_title = "Please contact us...."
    return render(request,"hello_world.html",{"title": my_title})
