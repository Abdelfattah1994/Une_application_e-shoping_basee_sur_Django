from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('produits/', views.produits),
    path('produit/details/<int:id>', views.detailsProduit),
    path('commandes/personne/<int:id>', views.commandePersonne),
    path('produit/nom/<str:name>', views.searchbyname),

]