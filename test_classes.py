import importlib

modules = ["Carre", "Cercle", "Triangle", "Lozange"]
required_methods = ["aire", "afficher", "dessiner"]

for mod_name in modules:
    try:
        mod = importlib.import_module(mod_name)
        cls = getattr(mod, mod_name)
        missing = [m for m in required_methods if not hasattr(cls, m)]
        if missing:
            print(f"❌ {mod_name} manque: {', '.join(missing)}")
        else:
            print(f"✅ {mod_name} OK")
    except Exception as e:
        print(f"❌ {mod_name} erreur: {e}")