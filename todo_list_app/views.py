from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("todo_list_app index")
