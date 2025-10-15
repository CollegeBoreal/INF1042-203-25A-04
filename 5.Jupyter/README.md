# :ringed_planet: Jupyter

Installer **Jupyter** (Notebook ou Lab) sous **Windows PowerShell**, en utilisant **Chocolatey**.

Voici la méthode **complète, stable et propre**, adaptée à ton installation actuelle (avec **Miniforge3** déjà installé par `choco`).

---

## 🧰 1. Vérifie que Miniforge est bien installé

Ouvre PowerShell (pas besoin d’administrateur) et tape :

```powershell
where conda
```

➡️ Si tu vois un chemin comme
`C:\ProgramData\Miniforge3\Scripts\conda.exe`
✅ tu es prêt.
Sinon, ajoute-le au PATH :

```powershell
$env:Path += ";C:\ProgramData\Miniforge3;C:\ProgramData\Miniforge3\Scripts"
```

---

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

---

## ⚙️ Alternative pure Chocolatey (sans Conda)

Si tu ne veux pas utiliser Conda, tu peux aussi faire :

```powershell
choco install python jupyter -y
```

Mais cette méthode n’utilise **pas les environnements isolés** (donc moins recommandée pour les cours et projets multiples).

