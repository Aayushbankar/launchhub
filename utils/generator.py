import os
import shutil
from pathlib import Path
from utils.template_engine import parse_and_replace_tokens



def generate_html_project(project_name, base_path="projects"):
    current_dir = Path.cwd()
    template_dir = current_dir / "templates" / "html"
    output_dir = current_dir / base_path / project_name

    if output_dir.exists():
        print(f"[!] Project '{project_name}' already exists at {output_dir}")
        return

    try:
        # Copy entire HTML template folder
        shutil.copytree(template_dir, output_dir)

        # Add .env
        with open(output_dir / ".env", "w") as f:
            f.write("ENV=development\nDEBUG=true\n")

        # Add .gitignore
        with open(output_dir / ".gitignore", "w") as f:
            f.write(".env\n__pycache__/\n*.pyc\n.DS_Store\n")

        # Replace {{project_name}} in index.html
        index_file = output_dir / "index.html"
        if index_file.exists():
            parse_and_replace_tokens(index_file, context={"project_name": project_name})


        # Replace {{project_name}} in assets/js/main.js
        js_file = output_dir / "assets" / "js" / "main.js"
        if js_file.exists():
            # js_file.write_text(js_file.read_text().replace("{{project_name}}", project_name))
            parse_and_replace_tokens(js_file, context={"project_name": project_name})

        # Replace {{project_name}} in README.md (optional)
        readme_file = output_dir / "README.md"
        if readme_file.exists():
            # readme_file.write_text(readme_file.read_text().replace("{{project_name}}", project_name))
            parse_and_replace_tokens(readme_file, context={"project_name": project_name})

        print(f"[✅] Project '{project_name}' created at: {output_dir}")
        return output_dir


    except Exception as e:
        print(f"[ERROR] Project generation failed: {e}")
        return None




def generate_flask_project(project_name, base_path="projects"):
    current_dir = Path.cwd()
    template_dir = current_dir / "templates" / "flask"
    output_dir = current_dir / base_path / project_name

    if output_dir.exists():
        print(f"[!] Project '{project_name}' already exists at {output_dir}")
        return None

    try:
        shutil.copytree(template_dir, output_dir)

        # Prepare context
        context = {"project_name": project_name}

        # Replace tokens in everything EXCEPT `.html` inside `templates/`
        for file in output_dir.rglob("*"):
            if file.is_file() and file.suffix != ".html":
                parse_and_replace_tokens(file, context)

        print(f"[✅] Project '{project_name}' created at: {output_dir}")
        return output_dir

    except Exception as e:
        print(f"[ERROR] Failed to generate Flask project: {e}")
        return None

