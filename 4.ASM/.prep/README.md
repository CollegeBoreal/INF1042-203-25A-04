# 4. Assembleur (Assembly - ASM)

## 🧩 — Introduction to Logic Circuits

### 🎯 Objectif du chapitre

Ce chapitre introduit les **circuits logiques combinatoires**, c’est-à-dire les circuits dont les sorties dépendent uniquement des **valeurs actuelles des entrées** (pas de mémoire).
Il établit le lien entre les **fonctions logiques** (mathématiques booléennes) et leur **implémentation matérielle** (portes logiques [Logic Gates], circuits physiques).

---

### 1. 💡 Concepts de base

* **Circuit logique** : réseau de **portes logiques** (AND, OR, NOT, etc.) qui manipulent des signaux binaires (0 et 1).
* **Variables binaires** : peuvent prendre la valeur `0` (faux) ou `1` (vrai).
* **Logique booléenne** : utilisée pour décrire le comportement des circuits.

---

### 2. 🧮 Fonctions logiques

* Une **fonction logique** est une expression reliant des entrées binaires à une sortie binaire.
* Peut être représentée sous plusieurs formes :

  * **Table de vérité**
  * **Expression booléenne**
  * **Diagramme logique**

Exemple :
Si $$f = x_1·x_2 + \bar{x_3}$$, cela signifie :
$$f = (x_1 \text{ AND } x_2) \text{ OR } (\text{ NOT } x_3)$$

---

### 3. 🔧 Portes logiques (Logic Gates) fondamentales

Les portes physiques de base sont :

* **NOT** (inversion)
* **AND** (conjonction)
* **OR** (disjonction)

Portes dérivées :

* **NAND** (NOT AND), **NOR** (NOT OR), **XOR** (Combinaison NOT et OR), **XNOR**

**NAND** et **NOR** sont dites **universelles** : on peut construire tout autre circuit à partir d’elles seules.

---

### 4. 🧱 Mise en œuvre de circuits logiques

* À partir d’une **table de vérité**, on déduit l’expression booléenne correspondante.
* Deux formes standards :

  * **Sum of Products (SOP)** : somme (OR) de termes produits (AND).
    Exemple : $$f(x_1,x_2) = \bar{x}_1x_2 + x_1\bar{x}_2$$
  * **Product of Sums (POS)** : produit (AND) de sommes (OR).
    Exemple : $$f(x_1,x_2) = (x_1 + x_2)(\bar{x}_1 + \bar{x}_2)$$
* Ces formes peuvent ensuite être simplifiées pour réduire le nombre de portes nécessaires.

---

### 5. ⚙️ Simplification des circuits

Méthodes utilisées :

* **Algèbre booléenne** : appliquer des lois (commutative, distributive, absorption, De Morgan, etc.)
* **Karnaugh maps (K-maps)** : représentation graphique permettant de simplifier visuellement une fonction logique à 4 ou 5 variables.

---

### 6. 🔌 Circuits combinatoires courants

Le chapitre présente des **blocs logiques standards** :

* **Encodeurs / Décodeurs**
* **Multiplexeurs (MUX)**
* **Démultiplexeurs**
* **Comparateurs**
* **Additionneurs (half-adder, full-adder)**

Ces blocs sont souvent utilisés comme **composants de base** dans des circuits plus complexes.

---

### 7. 🧠 Introduction à l'assembleur

* Le chapitre introduit brièvement **ASM** l'assembleur pour **décrire et simuler** instructions machines utilisant les circuits logiques.
* Les éléments essentiels :

  * **Tag** : définit les étiquettes.
  * **Register** : décrit les registres interne.
  * **Instructions** : permettent d’écrire des instructions en assembleur.

Exemple simple :


---

### ✅ En résumé

Le Chapitre établit les **fondations du raisonnement logique en électronique numérique** :

* Comprendre les **relations entre fonctions booléennes et circuits physiques**.
* Savoir **traduire une table de vérité en schéma logique**.
* Apprendre à **simplifier et modéliser** les circuits en **ASM**.
