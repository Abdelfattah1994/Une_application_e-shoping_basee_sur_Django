from django.db import models


class Categorie(models.Model):
    nomCat = models.CharField(max_length=30)


class Personne(models.Model):
    nomPersonne = models.CharField(max_length=30)
    prenomPersonne = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


class Produit(models.Model):
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        null=True
    )
    produitRef = models.CharField(max_length=30)
    nomProduit = models.CharField(max_length=30)
    dateProduction = models.DateField()
    prix = models.FloatField()


class Commande(models.Model):
    personne = models.ForeignKey(
        Personne,
        on_delete=models.CASCADE,
        null=True
    )
    produits = models.ManyToManyField(Produit)
    referenceCmd = models.CharField(max_length=30)
    dateCmd = models.DateField()
