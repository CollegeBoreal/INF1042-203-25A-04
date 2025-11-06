
# :ringed_planet: Jupyter

[:tada: Participation](.scripts/Participation.md)

Installer **Jupyter** (Notebook ou Lab) sous **Windows PowerShell**, en utilisant **Chocolatey**.

Installer **Miniforge** via **Chocolatey** sur Windows, voici la procédure complète :

---

### 1️⃣ Commande de base

Pour installer Miniforge pour **tous les utilisateurs** (AllUsers) et utiliser les valeurs par défaut :

```powershell
choco install miniforge3 -y
```

* `/AddToPath` par défaut est `0` pour AllUsers (il ne mettra pas Miniforge dans le PATH pour des raisons de sécurité).
* Le chemin par défaut sera : `C:\tools\miniforge3`

* L’installation se fera dans :
  `C:\Users\<TonNom>\AppData\Local\miniforge3`
* Python de Miniforge sera accessible directement depuis PowerShell.

---

### 3️⃣ Vérifier l’installation

Après installation, ferme et rouvre PowerShell puis tape :

```powershell
conda --version
```

si ça ne marche pas ajoute la variable d'environnement:

```powershell
$env:Path += ";C:\tools\miniforge3;C:\tools\miniforge3\Scripts"
```

Tu devrais voir la version de Conda.

## 🧩 2. (Optionnel) Mets à jour Conda

Toujours dans PowerShell :

```powershell
conda update -n base -c defaults conda -y
```

---

## 📦 3. Crée un environnement Python pour Jupyter

C’est préférable pour éviter les conflits de versions.

```powershell
conda create -n INF1042-203-25A-04 python=3.12 -y
conda activate INF1042-203-25A-04
```

---

## 🧠 4. Installe **JupyterLab (plus moderne)**

```powershell
conda install -c conda-forge jupyterlab -y
```

Puis lance-le avec :

```powershell
jupyter lab
```

---

## 🧭 5. (Optionnel) Ajoute un raccourci PowerShell pour l’ouvrir rapidement

Tu peux ajouter ceci à ton profil PowerShell :

```powershell
notepad $PROFILE
```

Puis ajoute à la fin du fichier :

```powershell
function start-jupyter {
    conda activate INF1042-203-25A-04
    jupyter lab
}
```

Ainsi tu pourras simplement taper :

```powershell
start-jupyter
```

à n’importe quel moment.

---

## 🧹 6. Vérifie ton installation

```powershell
jupyter --version
python --version
```

Tu devrais voir des versions cohérentes (par ex. Python 3.12.x et Jupyter 7.x ou 8.x).

# :books: References


