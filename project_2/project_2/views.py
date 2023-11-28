from django.shortcuts import render
import datetime

def home(req) :
    d = {"name" : "abir", "age" : 35, "des" : "I'm a software developer", "gf" : "", "lst" : ["Python", "is", "best"], "birthdate" : datetime.datetime.now(), "course" : [
        {
            "id" : 101,
            "courseName" : "python",
            "fee" : 5000
        },
        {
            "id" : 102,
            "courseName" : "mysql",
            "fee" : 4000
        },
        {
            "id" : 103,
            "courseName" : "django",
            "fee" : 7000
        }
    ]}
    return render(req, 'home.html', d)