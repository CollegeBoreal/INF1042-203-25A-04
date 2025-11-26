{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26c1790a-38f3-4a3f-b48c-a0af7b425770",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Fichier : Carre.py\n",
    "Description : Classe Carré héritant de Figure\n",
    "Auteur : [ID de l'étudiant]\n",
    "Date : YYYY-MM-DD\n",
    "\"\"\"\n",
    "\n",
    "from figure import Figure\n",
    "\n",
    "class Carre(Figure):\n",
    "    def __init__(self, cote):\n",
    "        super().__init__(\"Carré\")  # Appel du constructeur de la classe de base\n",
    "        self.cote = cote           # Longueur du côté du carré\n",
    "\n",
    "    def aire(self):\n",
    "        # Calcul de l'aire du carré\n",
    "        return self.cote ** 2\n",
    "\n",
    "    def afficher_info(self):\n",
    "        # Retourne une chaîne contenant le nom, le côté et l'aire\n",
    "        return f\"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}\"\n"
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
