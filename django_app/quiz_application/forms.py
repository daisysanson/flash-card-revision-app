from django.forms import ModelForm
from .models import Card, Deck

class DeckForm(ModelForm):
	class Meta:
		model = Deck
		fields = ['title']

class CardForm(ModelForm):
	class Meta:
		model = Card
		fields = ['question', 'answer']