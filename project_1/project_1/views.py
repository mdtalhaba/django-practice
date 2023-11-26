from django.http import HttpResponse

def home(req):
    return HttpResponse("This is Home")

def contact(req):
    return HttpResponse("This is Contact")