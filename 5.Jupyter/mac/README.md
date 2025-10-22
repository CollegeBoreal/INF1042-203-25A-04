# 🪐 Jupyter

You already have **Miniforge** installed via **Homebrew**, which means you also have `conda` and `mamba` (a faster alternative) available.

Let’s set up and run **Jupyter** step-by-step.

---

### 🧩 Step 1: Initialize Conda for your shell

Run this in your terminal:

```bash
conda init "$(basename "${SHELL}")"
```

Then restart your terminal (close and reopen).
This ensures that `conda` activates automatically and modifies your `$PATH` properly.

You can confirm with:

```bash
conda --version
```

---

### 🧠 Step 2: Create a dedicated environment for Jupyter

You can either use `conda` or the faster `mamba` (they’re interchangeable).

Example:

```bash
conda create -n jupyterlab-env python=3.11 jupyterlab -y
```

or equivalently:

```bash
mamba create -n jupyterlab-env python=3.11 jupyterlab -y
```

Activate it:

```bash
conda activate jupyterlab-env
```

---

### 🚀 Step 3: Launch JupyterLab

Once the environment is active:

```bash
jupyter lab
```

It will open **JupyterLab** in your browser (default: `http://localhost:8888`).

---

### 🧰 Optional — Classic Notebook Interface

If you prefer the older interface:

```bash
conda install notebook -y
jupyter notebook
```

---

### 🧼 Step 4: (Optional) Clean up or list environments

List environments:

```bash
conda env list
```

Remove one:

```bash
conda remove -n jupyterlab-env --all
```
