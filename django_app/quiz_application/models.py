from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class Author(models.Model):
    name = models.TextField()

    
    def __str__(self):
        return self.name

class Deck(models.Model):
    # author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')

    

    def __str__(self):
        return self.name

    def get_cards_num(self):
        cards = Card.objects.get_cards_to_study(user=self.Author, deck_id=self.id)
        return len(cards)


class Card(models.Model):
    # author = models.ForeignKey(author, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    consec_correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.question

