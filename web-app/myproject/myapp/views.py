
from django.shortcuts import render
from myapp.models import User

def hello(request):
    return render(request, "hello.html", {"name": "Jean"})


def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})