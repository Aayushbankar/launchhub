from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", project_name="{{project_name}}", author="{{author}}")

if __name__ == "__main__":
    app.run(debug=True)
