from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("""<h1>Hey I am a Django Server</h1>
                        <p> Hey this id from p tag </p>
                        <hr>
                        <h3 style="color:red">Hope you are loving it :) </h3>
                        
                        
                        """)

def sucess_page(request):
    print("*"*20)
    return HttpResponse("<h1>from sucess page<h2>")


def html_page(request):
    return render(request, "index.html")