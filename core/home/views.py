from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    peoples = [
        {'name' : 'Abhijeet', 'age':26},
        {'name' : 'Harsha', 'age':27},
        {'name' : 'Sandeep', 'age':16},
        {'name' : 'Arun', 'age':78},
        {'name' : 'Vicky', 'age':67}
        ]
    
    vegetables = ["Pumpkin","tomato", "Potato"]


    return render(request, "index.html",context = {'page':'Made with Django','peoples':peoples, "vegetables":vegetables})


def sucess_page(request):
    print("*"*20)
    return HttpResponse("<h1>from sucess page<h2>")


def html_page(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html",context={'page':'About'})

def contact(request):
    return render(request,"contact.html",context={'page':'Contact'})