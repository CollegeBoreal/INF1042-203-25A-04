# start-jupyter.ps1
# Lance JupyterLab directement dans le dossier du cours INF1042-203-25A-04

# Active l'environnement Conda du cours
conda activate INF1042-203-25A-04

# Définit le dossier d'ouverture de Jupyter
$JupyterPath = "C:\Users\user\Developer\INF1042-203-25A-04\5.Jupyter"

# Démarre JupyterLab dans ce dossier
Start-Process jupyter -ArgumentList "lab", "--notebook-dir=$JupyterPath"
