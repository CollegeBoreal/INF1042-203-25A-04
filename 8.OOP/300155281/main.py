{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "64317c9b-2385-4d91-9142-51443351e250",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'Carre'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m--------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m      2\u001b[39m \u001b[33;03mFichier : main.py\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[33;03mDescription : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.\u001b[39;00m\n\u001b[32m      4\u001b[39m \u001b[33;03mAuteur : [ID de l'étudiant]\u001b[39;00m\n\u001b[32m      5\u001b[39m \u001b[33;03mDate : YYYY-MM-DD\u001b[39;00m\n\u001b[32m      6\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mCarre\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Carre\n\u001b[32m      9\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mCercle\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m Cercle\n\u001b[32m     11\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mmain\u001b[39m():\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'Carre'"
     ]
    }
   ],
   "source": [
    "\n",
    "\"\"\"\n",
    "Fichier : main.py\n",
    "Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.\n",
    "Auteur : [ID de l'étudiant]\n",
    "Date : YYYY-MM-DD\n",
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
  },
  {
   "cell_type": "markdown",
   "id": "46f4f06f-826a-4947-8fed-a36f98b161ed",
   "metadata": {},
   "source": [
    "from Carre import Carre\n",
    "from Cercle import Cercle\n",
    "from Triangle import Triangle  # <-- votre nouvelle figure\n",
    "\n",
    "formes = [Carre(4), Cercle(3), Triangle(5, 2)]\n",
    "for f in formes:\n",
    "    print(f\"Aire: {f.aire()} 📏\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f993b63e-539b-4235-bf6e-703c0bfcc7c6",
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
