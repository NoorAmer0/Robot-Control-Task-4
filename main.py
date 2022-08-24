import json
from flask import Flask,render_template,request
import pyrebase

config = {
  "apiKey": "",
  "authDomain": "robotcontrol-f1519.firebaseapp.com",
  "databaseURL": "https://robotcontrol-f1519-default-rtdb.firebaseio.com",
  "storageBucket": ""
}
firebase = pyrebase.initialize_app(config)
app = Flask(__name__)



@app.route("/")
def main():
    return render_template("home.html")

@app.route("/report")
def displayReport():
    db_data =  firebase.database().child("date").get().val()
    return render_template("report.html",DB_Data = db_data)


@app.route('/test', methods=['POST'])
def storeInfo():
    info = json.loads(request.get_json()) #this converts the json output to a python dictionary

    firebase.database().child("date").child(info["date"]).child(info["time"]).set(info["direction"])
    return info
if __name__ == "__main__":
    app.run()

