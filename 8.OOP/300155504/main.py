# Signature : BadrEddine Barragoub - 300155504

"""
Fichier : main.py
Description : Programme de test pour la classe Carré.
Auteur : 300155504
Date : 2025-12-10
"""

from Carre import Carre  # مهم: C كبيرة بحال اسم الملف

def main():
    carre1 = Carre(4)
    carre2 = Carre(7)

    print(carre1.afficher_info())
    print(carre2.afficher_info())

if _name_ == "_main_":
    main()