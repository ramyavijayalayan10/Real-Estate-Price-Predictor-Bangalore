import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    global __locations
    print("DEBUG: Inside get_location_names, __locations =", __locations)
    return __locations

def load_saved_artifacts():
    global __locations
    global __data_columns
    global __model

    print("Loading saved artifacts...start")


    artifact_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'artifacts', 'columns_blr.json'))

    print("Loading JSON from:", artifact_path)
    with open(artifact_path, "r") as f:
        data = json.load(f)
        print("Loaded JSON keys:", data.keys())
        __data_columns = [col.lower() for col in data["data columns"]]
        __locations = __data_columns[3:]

    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'artifacts', 'Blr_house_price_prediction_model.pkl'))
    with open(model_path, "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st phase jp nagar", 1500, 3, 3))
    print(get_estimated_price("1st phase jp nagar", 1000, 2, 2))
    print(get_estimated_price("btm layout", 1500, 2, 3))
    print(get_estimated_price("bellandur", 1500, 2, 2))
    print(get_estimated_price("Indira Nagar", 1200, 3, 3))