from django.shortcuts import render

def index(req):
    return render(req, 'index.html')


# def home(req):
#     return HttpResponse("This is Home")

# def contact(req):
#     return HttpResponse("This is Contact")