from flask import Flask, render_template, request
from jd_parser import extract_skills
from generator import generate_questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jd_text = request.form["jd"]
        skills = extract_skills(jd_text)
        tech, hr, project = generate_questions(skills)
        return render_template(
            "index.html",
            skills=skills,
            tech=tech,
            hr=hr,
            project=project
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
