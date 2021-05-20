from flask import Flask, render_template,request,jsonify,redirect,url_for
import pymongo
from flask_pymongo import PyMongo
from decouple import config
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = config("MONGO_URI")
mongo=PyMongo(app)
tact_form = mongo.db.table

@app.route('/',methods=["POST","GET"])
def hello_world():
    return render_template("index.html")

@app.route("/add-details",methods=["POST","GET"])
def add_details():
    user_details={
        "Name" : request.values.get("Name"),
        "Collegename" : request.values.get("Collegename"),
        "Department" : request.values.get("Department"),
        "Year" : request.values.get("Year"),
        "emailaddress" : request.values.get("emailaddress"),
        "Contactnumber" : request.values.get("Contactnumber"),
        "knew about featurepreneur" : request.values.get("knew about featurepreneur")
    }
    tact_form.insert_one(user_details)
    return redirect(url_for('show_details'))

@app.route("/show-details",methods=["POST","GET"])
def show_details():
    return render_template("show.html",title="Submitted successfully")

if __name__=="__main__":
    app.run(debug=True)