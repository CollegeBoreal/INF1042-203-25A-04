
# :ringed_planet: Jupyter

[:tada: Participation](.scripts/Participation.md)

<details>
  <summary> :ringed_planet: <b>Table des matières</b> </summary>

- [📝 Jupyter et environnement Conda](#-jupyter-et-environnement-conda)
- [:a: 1. Installation](#a-installation)
- [🧩 2. (Optionnel) Mets à jour Conda](#-2-optionnel-mets-à-jour-conda)
- [📦 3. Crée un environnement Python pour Jupyter](#-3-crée-un-environnement-python-pour-jupyter)
- [🧠 4. Installe JupyterLab (plus moderne)](#-4-installe-jupyterlab-plus-moderne)
- [🧭 5. (Optionnel) Ajoute un raccourci PowerShell pour l’ouvrir rapidement](#-5-optionnel-ajoute-un-raccourci-powershell-pour-louvrir-rapidement)
- [🧹 6. Vérifie ton installation](#-6-vérifie-ton-installation)
- [:b: Expérimentation](#b-expérimentation)
- [:books: References](#books-references)

</details>



## 📝 Jupyter et environnement Conda

**Jupyter** n’est pas un IDE classique, mais une **interface interactive** qui permet de créer des **notebooks** contenant :

* du **code exécutable** (Python, R, Julia…)
* du **texte enrichi** (Markdown)
* des **visualisations et graphiques**

**Pourquoi créer un environnement Conda pour Jupyter ?**

Un **environnement Conda** est une **zone isolée** contenant sa propre version de Python et ses bibliothèques.

**Raisons principales :**

1. **Éviter les conflits** entre versions de Python ou bibliothèques pour différents projets.
2. **Reproductibilité** : ton environnement peut être partagé et reproduit exactement.
3. **Sécurité** : l’environnement de base reste propre et stable, sans risque de casser des dépendances.

> 💡 Astuce : chaque projet Jupyter doit idéalement avoir son propre environnement Conda pour garantir que les notebooks fonctionnent partout.

## :a: Installation

Pour Installer **Jupyter** (Notebook ou Lab) sous **Windows PowerShell**, en utilisant **Chocolatey**  et installer **Miniforge** via **Chocolatey** sur Windows, voici la procédure complète :

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
conda update --name base --channel defaults conda -y
```

---

## 📦 3. Crée un environnement Python pour Jupyter

C’est préférable pour éviter les conflits de versions.

:warning: Installer avec votre utilisateur, pas l'Administrateur  

```powershell
conda create --name INF1042-203-25A-04 python=3.12 -y
```
<details>

```lua
Channels:
 - conda-forge
Platform: osx-arm64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/homebrew/Caskroom/miniforge/base/envs/INF1042-203-25A-04

  added / updated specs:
    - python=3.12


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    libffi-3.5.2               |       he5f378a_0          39 KB  conda-forge
    python-3.12.12             |h18782d2_1_cpython        11.5 MB  conda-forge
    ------------------------------------------------------------
                                           Total:        11.5 MB

The following NEW packages will be INSTALLED:

  bzip2              conda-forge/osx-arm64::bzip2-1.0.8-hd037594_8 
  ca-certificates    conda-forge/noarch::ca-certificates-2025.10.5-hbd8a1cb_0 
  icu                conda-forge/osx-arm64::icu-75.1-hfee45f7_0 
  libexpat           conda-forge/osx-arm64::libexpat-2.7.1-hec049ff_0 
  libffi             conda-forge/osx-arm64::libffi-3.5.2-he5f378a_0 
  liblzma            conda-forge/osx-arm64::liblzma-5.8.1-h39f12f2_2 
  libsqlite          conda-forge/osx-arm64::libsqlite-3.50.4-h4237e3c_0 
  libzlib            conda-forge/osx-arm64::libzlib-1.3.1-h8359307_2 
  ncurses            conda-forge/osx-arm64::ncurses-6.5-h5e97a16_3 
  openssl            conda-forge/osx-arm64::openssl-3.5.4-h5503f6c_0 
  pip                conda-forge/noarch::pip-25.2-pyh8b19718_0 
  python             conda-forge/osx-arm64::python-3.12.12-h18782d2_1_cpython 
  readline           conda-forge/osx-arm64::readline-8.2-h1d1bf99_2 
  setuptools         conda-forge/noarch::setuptools-80.9.0-pyhff2d567_0 
  tk                 conda-forge/osx-arm64::tk-8.6.13-h892fb3f_2 
  tzdata             conda-forge/noarch::tzdata-2025b-h78e105d_0 
  wheel              conda-forge/noarch::wheel-0.45.1-pyhd8ed1ab_1 



Downloading and Extracting Packages:
                                                                                                                  
Preparing transaction: done                                                                                       
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate INF1042-203-25A-04
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

</details>

- [ ] Active ton environnement

```powershell
conda activate INF1042-203-25A-04
```

---

## 🧠 4. Installe **JupyterLab (plus moderne)**

```powershell
conda install --channel conda-forge jupyterlab -y
```

Puis lance-le avec :

```powershell
jupyter lab
```
<details>
<summary> :wood: **Log** </summary>

```lua
[I 2025-10-29 16:02:38.613 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2025-10-29 16:02:38.615 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2025-10-29 16:02:38.617 ServerApp] jupyterlab | extension was successfully linked.
[I 2025-10-29 16:02:38.811 ServerApp] notebook_shim | extension was successfully linked.
[I 2025-10-29 16:02:38.848 ServerApp] notebook_shim | extension was successfully loaded.
[I 2025-10-29 16:02:38.850 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2025-10-29 16:02:38.850 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2025-10-29 16:02:38.851 LabApp] JupyterLab extension loaded from /opt/homebrew/Caskroom/miniforge/base/envs/INF1042-203-25A-04/lib/python3.12/site-packages/jupyterlab
[I 2025-10-29 16:02:38.851 LabApp] JupyterLab application directory is /opt/homebrew/share/jupyter/lab
[I 2025-10-29 16:02:38.852 LabApp] Extension Manager is 'pypi'.
[I 2025-10-29 16:02:38.884 ServerApp] jupyterlab | extension was successfully loaded.
[I 2025-10-29 16:02:38.885 ServerApp] Serving notebooks from local directory: /Users/valiha/Developer/github.com/collegeboreal/INF1042-203-25A-04/5.Jupyter
[I 2025-10-29 16:02:38.885 ServerApp] Jupyter Server 2.17.0 is running at:
[I 2025-10-29 16:02:38.885 ServerApp] http://localhost:8888/lab?token=c5cab21cfaa688fc26731dc19561f2a604a7d6c899800312
[I 2025-10-29 16:02:38.885 ServerApp]     http://127.0.0.1:8888/lab?token=c5cab21cfaa688fc26731dc19561f2a604a7d6c899800312
[I 2025-10-29 16:02:38.885 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2025-10-29 16:02:38.896 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///Users/valiha/Library/Jupyter/runtime/jpserver-74934-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=c5cab21cfaa688fc26731dc19561f2a604a7d6c899800312
        http://127.0.0.1:8888/lab?token=c5cab21cfaa688fc26731dc19561f2a604a7d6c899800312
[I 2025-10-29 16:02:39.818 ServerApp] Skipped non-installed server(s): basedpyright, bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyrefly, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
[I 2025-10-29 16:02:41.090 LabApp] Build is up to date
```

</details>

* Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).


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

## :b: Expérimentation

### 🎛️ Créer un fichier dans ce répertoire `(5.Jupyter)`:

:checkered_flag: Finalement,

- [ ] Créer un répertoire avec :id: (votre identifiant boreal)
   - [ ] `mkdir ` :id:
- [ ] dans votre répertoire ajouter le fichier `README.md`
  - [ ] `nano `README.md
- [ ] envoyer vers le serveur `github.com`
  - [ ] `cd ..`
  - [ ] `git add `:id: 
  - [ ] `git commit -m "mon fichier ..."`
  - [ ] `git push`

### :rocket: Crée le fichier `RAPPORT.ipynb`

- [ ] Se diriger vers le répertoire avec :id: (votre identifiant boreal)
   - [ ] `cd ` :id:
- [ ] Dans `Jupyter` crée un fichier en `Python` et renomme le en `RAPPORT.ipynb`


# :books: References

<<<<<<< HEAD
## conda :snake:

- [ ] [Anaconda](https://github.com/CollegeBoreal/Tutoriels/tree/main/P.PackageManager/A.Anaconda)
=======
>>>>>>> e1d50e24795f641c3609493c501757d054c199a0

