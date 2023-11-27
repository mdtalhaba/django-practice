from django.shortcuts import render

def home(req) :
    d = {'name' : 'Rahim', 'age' : 35}
    return render(req, 'home.html',d)