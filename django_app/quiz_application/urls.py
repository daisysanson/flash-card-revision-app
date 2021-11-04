from django.urls import include, path, re_path
from . import views as views #importing our view file 

from django_app import settings
from django.conf.urls.static import static

from account.views import(
    registration_view,
)

urlpatterns = [
    path("", views.homepage, name="home"),
    path("view-card/<int:deck_id>", views.view_cards_by_deck, name="view-card"),
    path("view-card/<int:card_id>", views.view_cards, name="view-card"),
    path("view-decks/", views.viewdecks, name="view-decks"), 
    path("add-card/<int:deck_id>", views.addcard, name='add-card'),
    path("add-decks/", views.addDeck, name="add-decks"), 
    path("register/",registration_view,name="register")
    ] 