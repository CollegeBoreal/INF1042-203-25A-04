
from functools import reduce

def algebrique(liste):
    """
    Calcule la moyenne algébrique d'une liste en utilisant map/reduce pour additionner.
    
    :param liste: liste de nombres
    :return: moyenne algébrique
    """
    if not liste:
        return 0
    
    # Additionner tous les éléments avec reduce et lambda x + y
    # Calculer la moyenne
    return reduce(lambda x, y: x + y, liste) / len(liste)

def geometrique(liste):
    """
    Calcule la moyenne géométrique d'une liste de nombres positifs.
    
    :param liste: liste de nombres positifs
    :return: moyenne géométrique
    """
    if not liste:
        return 0
    
    # Vérifier que tous les nombres sont positifs
    if any(x <= 0 for x in liste):
        raise ValueError("Tous les nombres doivent être positifs pour la moyenne géométrique.")
    
    # Multiplier tous les éléments avec reduce
    # Calculer la racine n-ième
    return (reduce(lambda x, y: x * y, liste)) ** (1/len(liste))
