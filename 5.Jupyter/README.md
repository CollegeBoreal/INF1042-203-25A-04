# :ringed_planet: Jupyter

[:tada: Participation](.scripts/Participation.md)

Installer **Jupyter** (Notebook ou Lab) sous **Windows PowerShell**, en utilisant **Chocolatey**.

Installer **Miniforge** via **Chocolatey** sur Windows, voici la procédure complète :

---

### 1️⃣ Vérifier que Chocolatey est installé

Ouvre **PowerShell en mode Administrateur** et tape :

```powershell
choco --version
```

* Si tu vois un numéro de version, Chocolatey est déjà installé.
* Sinon, tu dois l’installer depuis [https://chocolatey.org/install](https://chocolatey.org/install).

---

### 2️⃣ Installer Miniforge

Toujours dans **PowerShell en Administrateur** :

```powershell
choco install miniforge3 -y
```

* `-y` : confirme automatiquement l’installation.
* Cela va installer Miniforge et ajouter `conda` au PATH.

---

### 3️⃣ Vérifier l’installation

Ferme PowerShell et rouvre-le (pour que le PATH soit pris en compte), puis tape :

```powershell
conda --version
```

Tu devrais voir un numéro de version, ce qui confirme que l’installation a réussi.

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

# :books: References


