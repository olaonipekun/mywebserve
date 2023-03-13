from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "myweb/index.html", {
    })

def greet(request, name):
    greetName = name
    return render(request, "myweb/greet.html", {
        "name": greetName.capitalize()
        })