from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load quiz questions
with open("questions.json", encoding="utf-8") as f:
    questions = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        user_answers = {}
        correct_answers = {}

        for q in questions:
            qid = q["id"]
            user_answer = request.form.get(qid)
            correct = q["answer"]
            user_answers[qid] = user_answer
            correct_answers[qid] = correct

            if user_answer == correct:
                score += 1

        return render_template(
            "result.html",
            score=score,
            total=len(questions),
            user_answers=user_answers,
            correct_answers=correct_answers,
            questions=questions
        )

    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
