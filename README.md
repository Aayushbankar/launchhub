
# 🚀 LaunchHub – Self-Bootstrapping Devstack Engine

LaunchHub is a Python-based CLI tool that generates complete project boilerplates across multiple stacks like HTML, Flask, and Python CLI. It’s designed for real-world developer workflows — fast, structured, repeatable.

---

## 📦 Supported Stacks (v0.4)

- `html` → Static frontend scaffold (HTML/CSS/JS)
- `flask` → Flask web app scaffold with Jinja2 templates
- `cli` → (Coming soon)

---

## ✅ Completed Increments

### Increment 1: HTML Generator  
- Command: `launchhub init html`
- Creates `index.html`, `assets/css/`, `assets/js/`, `.env`, `.gitignore`
- Injects `{{project_name}}`, `{{author}}`, etc.

---

### Increment 2: Template Engine  
- Parses any file for placeholders like `{{token}}`
- Prompts for missing values at runtime
- Replaces them safely in non-Jinja files

---

### Increment 2T: Unit Testing  
- Built-in test using `unittest` + `tempfile`
- Validates token injection logic

---

### Increment 3: Project Tracker  
- Logs each project into `launchhub.db`
- Records: name, stack, path, timestamp
- Command: `launchhub list`

---

### Increment 4A: Flask Stack Generator  
- Command: `launchhub init flask`
- Generates:
  - `app.py` with route logic
  - `templates/index.html` (Jinja2-safe)
  - `static/css/style.css`, `static/js/script.js`
  - `.env`, `.gitignore`, `README.md`
- Token injection applied to `app.py`, `.env`, etc.
- Jinja2 files skipped to preserve runtime logic

---

## 🛠 Usage

### Generate HTML Project
```bash
python3 launchhub.py init html
````

### Generate Flask Project

```bash
python3 launchhub.py init flask
```

### List Projects

```bash
python3 launchhub.py list
```

---

## 🔜 Next Increments

* CLI stack generator (argparse-based)
* Git auto-init + remote push
* Export logs to `.csv` / `.json`
* Plugin-based stack system

---

## 👤 Author

Crafted by Aayush Bankar
Structured. Automated. Developer-first.

```
