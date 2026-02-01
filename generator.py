import random
from question_bank import TECH_QUESTIONS, HR_QUESTIONS, PROJECT_QUESTIONS

def generate_questions(skills):
    tech = []

    for skill in skills:
        if skill in TECH_QUESTIONS:
            tech.extend(TECH_QUESTIONS[skill])

    tech = list(set(tech))
    tech = random.sample(tech, min(5, len(tech)))

    hr = random.sample(HR_QUESTIONS, 3)

    project = [
        q.format(skill=random.choice(skills))
        for q in PROJECT_QUESTIONS
    ] if skills else []

    return tech, hr, project
