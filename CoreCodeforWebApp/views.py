from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('''Welcome to the Course <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Click Here for navigating to Harry Coding</a> ''')

def removepunc(request):
    return HttpResponse("removepunc")
