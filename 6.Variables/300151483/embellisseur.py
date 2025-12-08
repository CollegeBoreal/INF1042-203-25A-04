{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d9f23e91-1815-4695-bd1a-7c355f06f87d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# embellisseur.py\n",
    "\n",
    "def f(x):\n",
    "    \"\"\"\n",
    "    Analyse une valeur et retourne ses caractéristiques principales.\n",
    "    \"\"\"\n",
    "    resultat = {\n",
    "        \"type\": type(x).__name__,\n",
    "        \"valeur\": x,\n",
    "        \"taille\": len(x) if hasattr(x, \"__len__\") else None,\n",
    "        \"est_numerique\": isinstance(x, (int, float)),\n",
    "        \"est_iterable\": hasattr(x, \"__iter__\"),\n",
    "    }\n",
    "    return resultat\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8a866fc-6278-4a7e-8203-aa3b3252a955",
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
