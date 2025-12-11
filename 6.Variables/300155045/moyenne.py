{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0737039b-d9cd-4dcb-8b47-1a40f997c51e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from functools import reduce\n",
    "\n",
    "def algebrique(liste):\n",
    "    \"\"\"\n",
    "    Calcule la moyenne algébrique d'une liste en utilisant map/reduce pour additionner.\n",
    "    \n",
    "    :param liste: liste de nombres\n",
    "    :return: moyenne algébrique\n",
    "    \"\"\"\n",
    "    if not liste:\n",
    "        return 0\n",
    "    \n",
    "    # Additionner tous les éléments avec reduce et lambda x + y\n",
    "    # Calculer la moyenne\n",
    "    return reduce(lambda x, y: x + y, liste) / len(liste)\n",
    "\n",
    "def geometrique(liste):\n",
    "    \"\"\"\n",
    "    Calcule la moyenne géométrique d'une liste de nombres positifs.\n",
    "    \n",
    "    :param liste: liste de nombres positifs\n",
    "    :return: moyenne géométrique\n",
    "    \"\"\"\n",
    "    if not liste:\n",
    "        return 0\n",
    "    \n",
    "    # Vérifier que tous les nombres sont positifs\n",
    "    if any(x <= 0 for x in liste):\n",
    "        raise ValueError(\"Tous les nombres doivent être positifs pour la moyenne géométrique.\")\n",
    "    \n",
    "    # Multiplier tous les éléments avec reduce\n",
    "    # Calculer la racine n-ième\n",
    "    return (reduce(lambda x, y: x * y, liste)) ** (1/len(liste))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "218cc7ad-3b22-4637-835a-5124782e7087",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8257e979-7f68-4c52-882c-7026faa83b7d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a0fc580-cf36-4645-ae90-5911b267124a",
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
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
