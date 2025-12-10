# 300155187 — Projet : Figures Géométriques en Python 📘 
## ✨ Introduction 
Ce projet présente une série de classes Python permettant de représenter et manipuler différentes figures géométriques en 2D et 3D. 
Chaque figure possède :  
- une classe dédiée (héritée de Figure)  
- une méthode d’affichage graphique utilisant matplotlib  
- une méthode pour calculer l’aire ou le volume  
- une méthode d’affichage d’informations
  
## 🔹 Figures 2D disponibles 
## ⬜ Carré 
  - Basé sur son côté 
## ⚪ Cercle 
  - Basé sur son rayon
## 🔶 Losange 
  - Basé sur ses diagonales
## ⬛ Parallélogramme 
- Basé sur sa base et sa hauteur
## 🔹 Figures 3D disponibles 
## 🛢️ Cylindre
     - Rayon r, Hauteur h 
## ⬛ Prisme carré 
    - Côté c, Hauteur h 
 ## 🔶 Prisme losange 
   - Diagonales d1, d2, Hauteur h 
 ## ▱ Prisme parallélogramme 
-  Base b, Hauteur h, Profondeur p 
## 🌐 Sphère 
  - Rayon r 
## 🔺 Cône 
Rayon r, Hauteur h 

## 🧩 Structure du Projet
```python
figure.py → Classe de base Figure  
carre.py → Classe Carre  
cercle.py → Classe Cercle  
losange.py → Classe Losange (d1, d2)  
parallelogramme.py → Classe Parallelogramme (b, h)  
cylindre.py → Classe Cylindre  
prisme_carre.py → Classe PrismeCarre  
prisme_losange.py → Classe PrismeLosange  
prisme_parallelogramme.py → Classe PrismeParallelogramme  
sphere.py → Classe Sphere  
cone.py → Classe Cone
``` 
## Fonctions d'affichage graphique : 

```python
afficher_carre()  
afficher_cercle()  
afficher_losange()  
afficher_parallelogramme()  
afficher_cylindre()  
afficher_prisme_carre()  
afficher_prisme_losange()  
afficher_prisme_parallelogramme()  
afficher_sphere()  
afficher_cone() 
```
## 🎯 Objectifs du Projet 
  - Appliquer les concepts de POO en Python  
  - Pratiquer l’héritage et les classes  
  - Visualiser les formes en 2D et 3D avec Matplotlib  
  - Calculer aires et volumes automatiquement  
  - Illustrer la représentation cartésienne
    
## 🟦 1. Carré ⬜ 
## 🧮 Classe 
  Le carré est défini par :
 - Attribut : cote  
 - une méthode : aire() = cote²

## 🖼️ Affichage 
La figure est tracée à partir des 4 sommets d’un carré dans le repère cartésien.
## ✨ Code d’affichage
```python
def afficher_carre(carre): 
    cote = carre.cote 
    x = [0, cote, cote, 0, 0] 
    y = [0, 0, cote, cote, 0] 
    plt.figure(figsize=(5, 5)) 
    plt.plot(x, y) 
    plt.fill(x, y, alpha=0.3) 
    plt.title(f"Carré — côté={cote}, aire={carre.aire()}") 
    plt.axis("equal") 
    plt.grid(True) 
    plt.show() 
```
## ⚪ 2. Cercle 
## 🧮 Classe 
  Le cercle est défini par :
- Attribut : rayon 
- Méthode : aire() = π × r²
  
## 🖼️ Affichage 
 Le contour du cercle est généré à partir de 300 points répartis sur un angle de 0 à 2π.
## ✨ Code d’affichage

```python
def afficher_cercle(cercle): 
    r = cercle.rayon 
    theta = np.linspace(0, 2*np.pi, 300) 
    x = r * np.cos(theta) 
    y = r * np.sin(theta) 
    plt.figure(figsize=(5, 5)) 
    plt.plot(x, y) 
    plt.fill(x, y, alpha=0.3) 
    plt.title(f"Cercle — rayon={r}, aire={cercle.aire():.2f}") 
    plt.axis("equal") 
    plt.grid(True) 
    plt.show() 
  ```

## 🔶 3. Losange 
## 🧮 Classe 
Le losange est défini par deux diagonales :
- d1 (la grande)
- d2 (la petite
## Aire :
```python
     A = (d1 × d2)/2
  ```
## 🖼️ Affichage 
```python
def afficher_losange(losange): 
    d1 = losange.d1 
    d2 = losange.d2 
    x = [0, d1/2, 0, -d1/2, 0] 
    y = [d2/2, 0, -d2/2, 0, d2/2] 
    plt.figure(figsize=(5, 5)) 
    plt.plot(x, y) 
    plt.fill(x, y, alpha=0.3) 
    plt.title(f"Losange — d1={d1}, d2={d2}, aire={losange.aire():.2f}") 
    plt.axis("equal") 
    plt.grid(True) 
    plt.show()
  ```
## ⬛ 4. Parallélogramme 
## 🧮 Classe 
  Le parallélogramme est défini par :
- b → base
- h → hauteur
  ## Aire :
  
```python
 A = b × h 
```
## 🖼️ Affichage 
Un décalage horizontal automatique (b/3) permet de créer un parallélogramme non-rectangle.
## ✨ Code d’affichage
```python
def afficher_parallelogramme(par): 
    b, h = par.b, par.h 
    d = b/3 
    x = [0, b, b+d, d, 0] 
    y = [0, 0, h, h, 0] 
    plt.figure(figsize=(5, 5)) 
    plt.plot(x, y) 
    plt.fill(x, y, alpha=0.3) 
    plt.title(f"Parallélogramme — base={b}, hauteur={h}, aire={par.aire():.2f}") 
    plt.axis("equal") 
    plt.grid(True) 
    plt.show()
```
## 🛢️ 5. Cylindre 
```python
def afficher_cylindre(cylindre): r, h = cylindre.rayon, cylindre.hauteur theta = np.linspace(0, 2np.pi, 50) z = np.linspace(0, h, 50) theta, z = np.meshgrid(theta, z) x = r * np.cos(theta) y = r * np.sin(theta) fig = plt.figure(figsize=(6,6)) ax = fig.add_subplot(111, projection='3d') ax.plot_surface(x, y, z, alpha=0.5) ax.plot_surface(rnp.cos(theta), rnp.sin(theta), np.zeros_like(theta), alpha=0.7) ax.plot_surface(rnp.cos(theta), rnp.sin(theta), hnp.ones_like(theta), alpha=0.7) ax.set_title(f"Cylindre — volume={cylindre.volume():.2f}") ax.set_box_aspect([1,1,1]) plt.show() 
```
## ⬛ 6. Prisme Carré

```python
def afficher_prisme_carre(p): 
    c, h = p.cote, p.hauteur 
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d') 
    x = [0, c, c, 0, 0] 
    y = [0, 0, c, c, 0] 
    z_bottom = [0]*5 
    z_top = [h]*5 
    ax.plot3D(x, y, z_bottom) 
    ax.plot3D(x, y, z_top) 
    for i in range(4): 
    ax.plot3D([x[i], x[i]], [y[i], y[i]], [0, h]) 
    ax.set_title(f"Prisme Carré — volume={p.volume():.2f}") 
    plt.show() 
```
## 🔶 7. Prisme Losange
```python
def afficher_prisme_losange(p): 
    d1, d2, h = p.d1, p.d2, p.hauteur 
    x = [0, d1/2, 0, -d1/2, 0] 
    y = [d2/2, 0, -d2/2, 0, d2/2] 
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d') 
    ax.plot3D(x, y, [0]*5) 
    ax.plot3D(x, y, [h]*5) 
    for i in range(4): 
    ax.plot3D([x[i], x[i]], [y[i], y[i]], [0, h]) 
    ax.set_title(f"Prisme Losange — volume={p.volume():.2f}") 
    plt.show() 
```
## ▱ 8. Prisme Parallélogramme 
```python
def afficher_prisme_parallelogramme(p): 
    b, h, prof = p.base, p.hauteur_parallelo, p.profondeur 
    d = b/3 
    x = [0, b, b+d, d, 0] 
    y = [0, 0, h, h, 0] 
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d') 
    ax.plot3D(x, y, [0]*5) 
    ax.plot3D(x, y, [prof]*5) 
    for i in range(4): 
    ax.plot3D([x[i], x[i]], [y[i], y[i]], [0, prof]) 
    ax.set_title(f"Prisme Parallélogramme — volume={p.volume():.2f}") 
    plt.show() 
  ```
## 🌐 9. Sphère

```python
def afficher_sphere(s): r = s.rayon theta, phi = np.linspace(0, np.pi, 40), np.linspace(0, 2*np.pi, 40) theta, phi = np.meshgrid(theta, phi) x = r * np.sin(theta) * np.cos(phi) y = r * np.sin(theta) * np.sin(phi) z = r * np.cos(theta) fig = plt.figure() ax = fig.add_subplot(111, projection='3d') ax.plot_surface(x, y, z, alpha=0.3) ax.set_title(f"Sphère — volume={s.volume():.2f}") plt.show() 
```
## 🔺 10. Cône 
```python
def afficher_cone(c): r, h = c.rayon, c.hauteur theta = np.linspace(0, 2np.pi, 50) z = np.linspace(0, h, 50) theta, z = np.meshgrid(theta, z) x = (r(1-z/h))np.cos(theta) y = (r(1-z/h))*np.sin(theta) fig = plt.figure() ax = fig.add_subplot(111, projection='3d') ax.plot_surface(x, y, z, alpha=0.3) ax.set_title(f"Cône — volume={c.volume():.2f}") plt.show() 
```

## 🧪 Démonstration générale

```python
c1 = Carre(4) 
c2 = Cercle(3) 
c3 = Losange(8,4) 
c4 = Parallelogramme(8,5) 
cy = Cylindre(2,5) 
pc = PrismeCarre(3,4) 
pl = PrismeLosange(4,6,5) 
pp = PrismeParallelogramme(4,3,5) 
s = Sphere(3) 
co = Cone(2,5)
```

```python
afficher_carre(c1) 
afficher_cercle(c2) 
afficher_losange(c3) 
afficher_parallelogramme(c4) 
afficher_cylindre(c5) 
afficher_prisme_carre(c6) 
afficher_prisme_losange(c7) 
afficher_prisme_parallelogramme(c8) 
afficher_sphere(c9) 
afficher_cone(c10)
``` 
## 🎉 Conclusion 
Ce projet montre : 
l’utilisation de la POO en Python 
l’héritage de classes 
la visualisation graphique 2D et 3D 
la géométrie analytique 
💡 Il constitue une base solide pour : 
Calculer périmètres et volumes 
Réaliser des transformations géométriques 
Ajouter coloriages et textures 
Créer des animations 2D et 3D interactives 

 

 

 








