from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
def index(request):
    return HttpResponse("voila une premiere vue django")

def produits(request):
     produits = Produit.objects.all()
     paginator = Paginator(produits, 10)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     title = 'liste des produits'
     context= {'produits': page_obj}
     return render(request, 'produits.html', context)

def detailsProduit(request, id):
    produit = Produit.objects.get(id = id)
    context = {'produit': produit}
    return render(request, 'detailsProduit.html',context)

def commandePersonne(request, id):
     per = Personne.objects.get(id=id)
     coms = Commande.objects.all().filter(personne=per)
     title = 'liste des Commandes dune personne'
     context = {'commandes': coms}
     return render(request, 'commandes.html', context)

def searchbyname(request, name):
     produits = Produit.objects.all().filter(nomProduit__contains=name)
     title = 'liste des produits ayant un nom'
     context = {'produits': produits}
     return render(request, 'produits.html', context)