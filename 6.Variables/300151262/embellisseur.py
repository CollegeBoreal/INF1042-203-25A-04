def f(x):
    'Démonstration de polymorphisme. Retourne un dict selon le type de x.'
    info = {'type': type(x).__name__, 'repr': repr(x)}
    if isinstance(x, (int, float)):
        info['is_numeric'] = True
        info['double'] = x * 2
    else:
        info['is_numeric'] = False
    if isinstance(x, (list, tuple, set)):
        info['length'] = len(x)
        try:
            info['sum_if_numeric'] = sum(x)
        except TypeError:
            info['sum_if_numeric'] = None
    if isinstance(x, dict):
        info['keys'] = list(x.keys())
        info['values'] = list(x.values())
    if isinstance(x, str):
        info['length'] = len(x)
        info['upper'] = x.upper()
    return info
