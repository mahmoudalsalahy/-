import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)


dt = pickle.load(open("DT.pkl", "rb"))



@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = dt.predict(features)
    if prediction==1:
       return render_template("index.html", prediction_text = "إصابتك بالسرطان متوسطة")
    if prediction==0:
        return render_template("index.html", prediction_text = "إصابتك بالسرطان ضعيفة")
    else:
        return render_template("index.html", prediction_text = "إصابتك بالسرطان عالية")
    
    
          
    

if __name__ == "__main__":
    flask_app.run(debug=True)