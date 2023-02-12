from flask import Flask, request, render_template,
from 

app = Flask(__name__)

responses = []

@app.route("/")
def home():
    """homepage w/ title and instructions"""

    return render_template("base.html")

@app.route("/questions/<int:question_id>", methods =[ "GET", "POST"])
def questions(question_id):
    if request.method = "GET" and question_id < 5:
        question = questions[questions_id]
        return render_template("questions.html", question=question, question_id=question_id )
    elif request.method = "POST":
        answer = request.form("answer")
        
        responses.append(answer)
    else 
        return render_template("thanks.html")

if __name__ == '__main__':
    app.run()








