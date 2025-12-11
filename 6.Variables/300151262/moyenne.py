from math import prod

def algebrique(L):
    'Moyenne arithmétique: sum(L)/len(L) si L non vide, sinon 0.'
    return sum(L) / len(L) if L else 0

def geometrique(L):
    'Moyenne géométrique: (prod(L))**(1/len(L)) si L non vide, sinon 0.'
    return (prod(L))**(1/len(L)) if L else 0
