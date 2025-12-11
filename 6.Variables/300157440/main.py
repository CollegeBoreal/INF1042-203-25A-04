{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f075642-f472-407c-bb31-c40d8962b87a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# main.py\n",
    "\"\"\"\n",
    "Script principal qui importe le module convertisseur et teste f(x)\n",
    "\"\"\"\n",
    "\n",
    "from embellisseur import f\n",
    "\n",
    "print(\"=== Démonstration de f(x) avec @singledispatch ===\\n\")\n",
    "\n",
    "exemples = [\n",
    "    10,\n",
    "    2.718,\n",
    "    \"hello\",\n",
    "    [7, 8, 9],\n",
    "    (10, 20, 30),\n",
    "    {\"x\": 1, \"y\": 2}\n",
    "]\n",
    "\n",
    "for e in exemples:\n",
    "    print(f\"\\n--- f({e}) ---\")\n",
    "    resultat = f(e)\n",
    "    for k, v in resultat.items():\n",
    "        print(f\"{k:12} -> {v}\")\n",
    "\n",
    "from convertisseur import convert_all\n",
    "\n",
    "print(\"=== convertir une liste ===\\n\")\n",
    "\n",
    "# Exemple : convertir une liste\n",
    "tests = {\n",
    "    \"binaire\": 8,\n",
    "    \"hexadécimal\": 255,\n",
    "    \"int\": \"42\",\n",
    "    \"float\": \"3.14\",\n",
    "    \"str\": 123,\n",
    "    \"list\": (1, 2, 3),\n",
    "    \"tuple\": [1, 2, 3],\n",
    "    \"array\": [4, 5, 6],\n",
    "    \"dict\": [(\"a\", 1), (\"b\", 2)]\n",
    "}\n",
    "\n",
    "for t, val in tests.items():\n",
    "    print(f\"\\n{t.upper()} : {val}\")\n",
    "    for name, result in convert_all(val):\n",
    "        if name == t:\n",
    "            print(f\"→ {result}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d654fa22-ca5c-4055-9a13-ea9faad666d2",
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
