# 🚀 LaunchHub – Self-Bootstrapping Devstack Engine

LaunchHub is a Python-based CLI tool that generates complete project boilerplates across multiple stacks like HTML, Flask, and Python CLI. It’s designed for real-world developer workflows — fast, structured, repeatable.

---

## 📦 Supported Stacks (v0.3)

- `html` → Generates a static frontend boilerplate  
- `flask` → Coming next  
- `cli` → Coming next  

---

## ✅ Completed Features

### Increment 1: HTML Generator  
- Command: `launchhub init html`
- Creates:
  - `index.html`, `assets/css/main.css`, `assets/js/main.js`
  - `.env`, `.gitignore`, `README.md`
- Auto-injects `{{project_name}}`

---

### Increment 2: Templating Engine  
- Dynamic token injection in any file  
- Supports:
  - `{{project_name}}`, `{{author}}`, `{{date}}`, etc.  
- Filters out unsafe tokens (e.g., Jinja2 `url_for()`)

---

### Increment 2T: Test Suite  
- Unit test for template engine  
- Uses `unittest` + `tempfile`  
- Ensures replacements are correct and safe

---

### Increment 3: Project Tracker  
- Local SQLite DB logs:
  - Project name  
  - Stack used  
  - Output path  
  - Timestamp  
- CLI Command: `launchhub list` shows log of all generated projects

---

## 🛠 Usage

### Create Project
```bash
python3 launchhub.py init html
````

Then:

```
Enter project name: my-site
Enter value for 'author': Aayush
Enter value for 'date': 2025-06-26
```

### List All Projects

```bash
python3 launchhub.py list
```

---

## 🔜 Next Milestone

### Increment 4 (Upcoming):

* Flask stack with:

  * `app.py`, `/templates`, `/static`
  * Jinja2-compatible template that skips token parsing
* CLI stack with:

  * `main.py`, `argparse`, help banners
* UI/UX templates for all 3

---

## 🧠 Philosophy

* No magic. No bloat.
* Local-first, developer-owned scaffolding engine
* Every file is real. Every feature is tested.
* Built to teach architecture, not just automate it.

---

## 👤 Author

Crafted by Aayush Bankar
Driven by systems thinking, autonomy, and the will to master.

```

