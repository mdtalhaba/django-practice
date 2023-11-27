from django.shortcuts import render

def home(req) :
    return render(req, 'first_app/home.html')


