Tagging the `main` branch (or any branch) is a common and safe way to **save a snapshot** of your repository at a known good point (e.g. before students push new work).

Here’s exactly how to do it:

---

## 🎯 **1️⃣ Create a tag on the main branch**

Make sure you’re on `main` and up to date:

```bash
git checkout main
git pull origin main
```

Then create a **lightweight tag** (simple label):

```bash
git tag v1.0
```

or an **annotated tag** (recommended — includes message, author, and date):

```bash
git tag -a v1.0 -m "Version stable avant modifications des étudiants"
```

---

## 🎯 **2️⃣ Verify the tag**

```bash
git tag
```

To see details:

```bash
git show v1.0
```

---

## 🎯 **3️⃣ Push the tag to GitHub (very important)**

By default, `git push` does **not** push tags. You must push them explicitly:

```bash
git push origin v1.0
```

Or push **all local tags**:

```bash
git push origin --tags
```

Now the tag appears on GitHub under the **“Tags”** section of your repository.

---

## 🎯 **4️⃣ Later, revert or check out this tag**

If needed, you can always restore that state:

```bash
git checkout v1.0
# (detached HEAD)
```

Or create a branch from it:

```bash
git checkout -b restore-v1.0 v1.0
```

---

### ✅ **Best practice for classroom repos**

* Before students start a new lab, you tag the main branch (e.g. `v1.0-lab1-start`).
* After verifying everyone’s work, tag the end state (e.g. `v1.0-lab1-final`).
* If a student overwrites something, you can instantly restore:

  ```bash
  git reset --hard v1.0-lab1-start
  git push --force origin main
  ```


