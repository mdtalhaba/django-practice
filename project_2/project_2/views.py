from django.shortcuts import render
import datetime

def home(req) :
    d = {"name" : "abir", "age" : 21, "des" : "I'm a software developer", "gf" : "", "lst" : ["Python", "is", "best"], "lst2" : [4, 5, 7, 9, 1, 2], "currentdate" : datetime.datetime.now(), "birthday" : datetime.datetime(2002, 3, 1), "course" : [
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