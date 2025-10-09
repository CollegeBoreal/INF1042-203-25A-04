# Assembleur (Assembly - ASM)

## 🧩 Chapitre 1 — Introduction to Logic Circuits

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
Si `F = A·B + ¬C`, cela signifie :
`F = (A AND B) OR (NOT C)`

---

### 3. 🔧 Portes logiques fondamentales

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
    Exemple : $$f = \bar{x}_1x_2 + x_1\bar{x_2}$$
  * **Product of Sums (POS)** : produit (AND) de sommes (OR).
    Exemple : `F = (A + B)(A’ + B’)`
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

### 7. 🧠 Introduction à VHDL

* Le chapitre introduit brièvement **VHDL** (VHSIC Hardware Description Language) pour **décrire et simuler** les circuits logiques.
* Les éléments essentiels :

  * **Entity** : définit les entrées/sorties du circuit.
  * **Architecture** : décrit le comportement logique interne.
  * **Concurrent statements** : permettent d’écrire des équations logiques directement.

Exemple simple :

```vhdl
entity and2 is
  port (A, B : in std_logic; F : out std_logic);
end entity;

architecture logic of and2 is
begin
  F <= A and B;
end architecture;
```

---

### ✅ En résumé

Le Chapitre 2 établit les **fondations du raisonnement logique en électronique numérique** :

* Comprendre les **relations entre fonctions booléennes et circuits physiques**.
* Savoir **traduire une table de vérité en schéma logique**.
* Apprendre à **simplifier et modéliser** les circuits en **VHDL**.

---

Souhaitez-vous que je te fasse un **résumé plus condensé (1 page)** ou une **fiche de révision structurée** (avec formules, lois booléennes et exemples types) ?
