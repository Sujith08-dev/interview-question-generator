# interview-question-generator
A Flask-based web application that generates role-specific interview questions by analyzing job descriptions using rule-based NLP.
# Interview Question Generator from Job Description

A Python Flask web application that helps candidates prepare for interviews by generating role-specific interview questions based on a given job description.

## Features
- Extracts technical skills from job descriptions using rule-based NLP (regex)
- Generates technical, HR, and project-based interview questions
- Preserves user input across requests
- Clean and responsive UI using HTML and CSS

## Tech Stack
- Python
- Flask
- HTML, CSS
- Regex
- Jinja2

## How It Works
1. User pastes a job description
2. Application extracts relevant skills
3. Questions are generated based on detected skills
4. Results are displayed on the same page

## How to Run
```bash
pip install flask
python app8.py

