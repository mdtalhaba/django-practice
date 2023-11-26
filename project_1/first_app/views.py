from django.shortcuts import render
from django.http import HttpResponse

def home(res) :
    return HttpResponse("This is first app. ")

def courses(res) :
    return HttpResponse("This is first app Courses Page. ")

def about(res) :
    return HttpResponse("This is first app about page. ")
