from flask import Flask, render_template
from flask import request ,url_for,redirect
import csv

# $env:FLASK_APP = "server.py"
# flask run
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/works.html")
def work():
    return render_template("works.html")

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

#BELOW HERE IS HOW WE ARE STORING THE DATA
def write_to_csv(data):
    with open("database.csv",newline='', mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=",",quotechar=";",quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])#post means browser wants us to save info, while get wants us to send info
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")


