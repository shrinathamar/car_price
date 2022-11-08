import numpy as np
import config
import json
import pickle
import joblib 


class CarPricePrediction:

    def __init__(self, year, km_driven, owner, mileage, engine, max_power, torque, seats, transmission, fuel, seller, brand):
        self.year = year
        self.km_driven = km_driven
        self.owner    = owner
        self.mileage   = mileage
        self.engine = engine
        self.max_power = max_power
        self.torque  = torque
        self.seats = seats
        self.transmission = "transmission_" + transmission
        self.fuel =  "fuel_" + fuel 
        self.seller = "seller_type_" + seller
        self.brand = brand


    def load_data(self):
        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_DATA_PATH, "r") as f:
            self.columns_name = json.load(f)
    def get_brand_names(self):
        self.load_data()
        return self.columns_name["columns"][17:]

    def predict_car_price(self):
        self.load_data()

        test_array = np.zeros(49)

        test_array[0] = self.year               # year age of car
        test_array[1] = self.km_driven          # kms driven
        test_array[2] =  self.columns_name["owener"][self.owner]
        test_array[3] =  self.mileage          #'mileage'
        test_array[4] = self.engine             #engine
        test_array[5] = self.max_power           #max_power
        test_array[6] = self.torque            #torque
        test_array[7] = self.seats             #seats

        idx = self.columns_name["columns"].index(self.transmission)
        test_array[idx] = 1

        idx_fuel = self.columns_name["columns"].index(self.fuel)
        test_array[idx_fuel] = 1


        idx_sell = self.columns_name["columns"].index(self.seller)
        test_array[idx_sell] = 1


        idx_na = self.columns_name["columns"].index(self.brand)
        test_array[idx_na] = 1
        
        print(test_array)
        car_price  = self.model.predict([test_array])
        
        return car_price

