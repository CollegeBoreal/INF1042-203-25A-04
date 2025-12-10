{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9dc85e75-5aae-458a-9103-c465f919db70",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Fichier : main.py\n",
    "Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.\n",
    "Auteur : [300156615]\n",
    "Date : 2025-12-06\n",
    "\"\"\"\n",
    "\n",
    "from Carre import Carre\n",
    "from Cercle import Cercle\n",
    "\n",
    "def main():\n",
    "    \"\"\"\n",
    "    Fonction principale du programme.\n",
    "    Crée un carré et un cercle, puis affiche leurs informations.\n",
    "    \"\"\"\n",
    "    # Création d'un carré de côté 4\n",
    "    c1 = Carre(4)\n",
    "\n",
    "    # Création d'un cercle de rayon 3\n",
    "    c2 = Cercle(3)\n",
    "\n",
    "    # Affichage des informations des deux figures\n",
    "    print(c1.afficher_info())\n",
    "    print(c2.afficher_info())\n",
    "\n",
    "# Point d'entrée du programme\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
