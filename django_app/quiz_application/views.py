from django.shortcuts import render, redirect
from .models import Card, Deck
import logging
from .forms import CardForm, DeckForm
from django.http import request, HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger = logging.getLogger(__name__)

def homepage(request):
  user = request.user
  context = { "user" : user }
  return render(request, 'index.html', context)

def addDeck(request):
  if request.user.is_authenticated:
        all_cards = Card.objects.filter(author=request.user.id)
  else:
       redirect('login')
  if request.method == 'POST':
    form = DeckForm(request.POST)
    if form.is_valid():
      new_deck = form.save(commit=False)
      new_deck.author = request.user
      new_deck.save()
      return render (request, 'add-decks.html', {"new-decks": new_deck}) 
  else:
      form = DeckForm()

  return render(request,'add-decks.html', {"form":form})

def addcard(request, deck_id):
  form = CardForm(request.POST)
  deck_id = Deck.objects.get(id=deck_id)
  if request.method == 'POST':
        if form.is_valid():
          new_card = form.save(commit=False)
          new_card.author = request.user
          new_card.deck = deck_id
          new_card.save()
          return redirect('home')
  else:
    form = CardForm()
  return render(request,'add-card.html', {"form":form, 'deck_id': deck_id})

def view_cards_by_deck(request, deck_id):
  all_cards = Card.objects.filter(deck=deck_id)  
  paginator = Paginator(all_cards, 1)
  page = request.GET.get('page')
  
  try:
      cards = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer get the first page
       cards = paginator.page(1)
  except EmptyPage:
    # If page is out of range get last page of results
      cards = paginator.page(paginator.num_pages)
  context = {'deck_id':deck_id, "cards":cards, 'page':page}
  return render(request, 'view-card.html', context)

def view_cards(request, card_id):
   if request.user.is_authenticated:
        card = Card.objects.get(id=card_id)
   else:
        all_cards = Card.objects.all()

   context = {'card': card}
   return render(request, 'view-card.html', context)
  
  
def viewdecks(request):
  all_decks = Deck.objects.filter(author=request.user.id)
  context = {'decks': all_decks}
  return render(request, 'view-decks.html', context)
