{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc9c7784-c6d7-4ca4-8bb0-8a744f08bb38",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Fichier : Cercle.py\n",
    "Description : Classe Cercle héritant de Figure\n",
    "Auteur : [ID de l'étudiant]\n",
    "Date : YYYY-MM-DD\n",
    "\"\"\"\n",
    "\n",
    "from figure import Figure\n",
    "import math\n",
    "\n",
    "class Cercle(Figure):\n",
    "    def __init__(self, rayon):\n",
    "        super().__init__(\"Cercle\")  # Appel du constructeur de la classe de base\n",
    "        self.rayon = rayon           # Rayon du cercle\n",
    "\n",
    "    def aire(self):\n",
    "        # Calcul de l'aire du cercle\n",
    "        return math.pi * self.rayon ** 2\n",
    "\n",
    "    def afficher_info(self):\n",
    "        # Retourne une chaîne contenant le nom, le rayon et l'aire\n",
    "        return f\"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}\""
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
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
