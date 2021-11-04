from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

class Deck(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	title = models.TextField()
	class Meta:
		managed = True
		db_table = 'Deck'

class Card(models.Model):
	deck = models.ForeignKey(Deck, on_delete=models.CASCADE, blank=True, null=True)
	question = models.TextField()
	answer = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	learned = models.IntegerField(default=0)

	def __str__(self):
		return self.answer
	class Meta:
		managed = True
		db_table = 'Card'

class CardToDeck(models.Model):
	deck = models.ForeignKey(Deck, on_delete=models.CASCADE, blank=True, null=True)
	card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True, null=True)





