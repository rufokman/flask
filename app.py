from flask import Flask, request, render_template
import pandas as pd
import joblib
from flask_bootstrap import Bootstrap


# Declare a Flask app
from models import QuizForm

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])


def main():

    # If a form is submitted
    if request.method == "POST":
        print(request)
        #form = QuizForm(request.form)

        # Unpickle classifier
        clf = joblib.load("diam_net.pkl")

        # Get values through input bars
        carat = request.form.get("carat")
        depth = request.form.get("depth")
        table = request.form.get("table")
        x = request.form.get("x")
        y = request.form.get("y")
        z = request.form.get("z")
        # carat = form.carat.data
        # depth = form.depth.data
        # table = form.table.data
        # x = form.x.data
        # y = form.y.data
        # z = form.z.data
        # Put inputs to dataframe
        print([carat,depth,table,x,y,z])
        X = pd.DataFrame([[carat,depth,table,x,y,z]], columns=["carat", "depth", 'table', 'x', 'y', 'z'])

        # Get prediction
        prediction = clf.predict(X)[0]
        return str(prediction)
    else:
        prediction = ""

    return render_template("website.html", output=prediction, )

# Running the app
if __name__ == '__main__':
    app.run(debug = True)