{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0330df97-46d2-4b8b-9ee2-bed9be19202c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'figure'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m      2\u001b[39m \u001b[33;03mFichier : Triangle.py\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[33;03mDescription : Classe Triangle héritant de Figure\u001b[39;00m\n\u001b[32m      4\u001b[39m \u001b[33;03mAuteur : [ID de l'étudiant]\u001b[39;00m\n\u001b[32m      5\u001b[39m \u001b[33;03mDate : YYYY-MM-DD\u001b[39;00m\n\u001b[32m      6\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mfigure\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Figure\n\u001b[32m     10\u001b[39m \u001b[38;5;28;01mclass\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mTriangle\u001b[39;00m(Figure):\n\u001b[32m     11\u001b[39m     \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m, base, hauteur):\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'figure'"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Fichier : Triangle.py\n",
    "Description : Classe Triangle héritant de Figure\n",
    "Auteur : [ID de l'étudiant]\n",
    "Date : YYYY-MM-DD\n",
    "\"\"\"\n",
    "\n",
    "from figure import Figure\n",
    "\n",
    "class Triangle(Figure):\n",
    "    def __init__(self, base, hauteur):\n",
    "        super().__init__(\"Triangle\")  # Appel du constructeur de la classe de base\n",
    "        self.base = base              # Longueur de la base\n",
    "        self.hauteur = hauteur        # Hauteur du triangle\n",
    "\n",
    "    def aire(self):\n",
    "        # Calcul de l'aire du triangle : (base * hauteur) / 2\n",
    "        return (self.base * self.hauteur) / 2\n",
    "\n",
    "    def afficher_info(self):\n",
    "        # Retourne une chaîne contenant le nom, la base, la hauteur et l'aire\n",
    "        return f\"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire()}\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "741efa8b-9c1e-4106-9afe-91577a4d3d6e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character '🆔' (U+1F194) (1953302535.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m🆔/\u001b[39m\n    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid character '🆔' (U+1F194)\n"
     ]
    }
   ],
   "source": [
    "🆔/\n",
    "├── figure.py\n",
    "├── Carre.py\n",
    "├── Cercle.py\n",
    "├── Triangle.py\n",
    "└── main.py\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f378113d-b9a9-44ad-a42c-38453f54e77a",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Fichier : figure.py\n",
    "Description : Classe de base pour toutes les figures géométriques\n",
    "Auteur : [ID de l'étudiant]\n",
    "Date : YYYY-MM-DD\n",
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
    "        raise NotImplementedError(\"Cette méthode doit être implémentée par les sous-classes.\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3b1d763-b60d-448c-bf5e-e647a4f2d98c",
   "metadata": {},
   "outputs": [],
   "source": []
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
