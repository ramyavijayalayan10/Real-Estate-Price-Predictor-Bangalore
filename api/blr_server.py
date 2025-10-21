from flask import Flask, request, jsonify, render_template
import os
import sys

# Append project root to sys.path so util_alt can be found if needed 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import util_alt as util

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../client')) 
app = Flask(__name__, template_folder=template_dir, static_folder=os.path.join(template_dir, 'static'))

@app.route('/') 
def home(): 
    return render_template('App.html')

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({"locations" : util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_house_price", methods = ['POST'])
def predict_house_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bath = int(request.form["bath"])
    bhk = int(request.form["bhk"])
    estimated_price = util.get_estimated_price(location, total_sqft, bath, bhk)

    response = jsonify({"estimated_price": estimated_price})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    print("Starting Python Flask server for House Price Prediction...")
    util.load_saved_artifacts()
    app.run()

