from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
    if 0>1:
        return render_template("index.html", title="")
    return redirect('/news')


@app.route("/news")
def news():
    return render_template("news.html", title="news")


@app.route("/feedback")
def deedback():
    return render_template("feedback.html", title="feedback")
