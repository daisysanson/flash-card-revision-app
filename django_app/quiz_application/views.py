from django.shortcuts import render, redirect
from .models import Card
from django.http import request, HttpRequest

def homepage(request):
  return render(request, 'index.html')

def addcard (request:HttpRequest):
  card = Card(content = request.POST['question','answer'])
  card.save()
  return viewcard

def viewcard (request):
  return render(request, 'viewcard.html',)