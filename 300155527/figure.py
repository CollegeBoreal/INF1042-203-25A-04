{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acd4e1b6-2765-4be9-b4e3-930ba4014029",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Fichier : figure.py\n",
    "Description : Classe de base pour toutes les figures géométriques\n",
    "Auteur : [300155527]\n",
    "Date : -10-20\n",
    "\"\"\"\n",
    "\n",
    "class Figure:\n",
    "    def __init__(self, nom):\n",
    "        # Nom de la figure (ex: Carré, Cercle)\n",
    "        self.nom = nom\n",
    "\n",
    "    def afficher_info(self):\n",
    "        # Retourne une chaîne contenant le nom de la figure\n",
    "        return f\"Figure: {self.nom}\"\n",
    "\n",
    "    def aire(self):\n",
    "        # Méthode à implémenter par les sous-classes\n",
    "        raise NotImplementedError(\"Cette méthode doit être implémentée par les sous-classes.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
