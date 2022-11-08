
from flask import Flask, request, jsonify, render_template
import config
from utils import  CarPricePrediction


# creating app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["GET", "POST"])
def predict_price():

    data = request.form

    year      = eval(data["year"])
    km_driven = eval(data["km_driven"])
    owner     =     data["owner"]
    mileage   = eval(data["mileage"])
    engine    = eval(data["engine"])
    max_power = eval(data["max_power"])
    torque    = eval(data["torque"])
    seats     = eval(data["seats"])
    transmission =  data["transmission"]
    fuel         =  data["fuel"]
    seller       =  data["seller"]
    brand        =  data["brand"]
 
    object = CarPricePrediction(year, km_driven, owner, mileage, engine, max_power, torque, seats, transmission, fuel, seller, brand )
    price = object.predict_car_price()
   


    return render_template("index2.html", price=round(price[0], 2))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUM2)
