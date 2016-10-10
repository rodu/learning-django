from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, "dashboard/home.html", {
    'message': 'Hi there!'
  })
