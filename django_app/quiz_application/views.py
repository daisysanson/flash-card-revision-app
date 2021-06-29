from django.shortcuts import render
from .models import Card

def homepage(request):
  return render(request, 'index.html', context={})


def new-card(request):
  return render(request, 'new-card.html')

# return response