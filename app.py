from flask import Flask, render_template
from logic.person_logic import PersonLogic

app = Flask(__name__)


@app.route("/")
def home():
    logic = PersonLogic()
    personList = logic.getAllPerson()
    return render_template("index.html", personList=personList)


if __name__ == "__main__":
    app.run(debug=True)
