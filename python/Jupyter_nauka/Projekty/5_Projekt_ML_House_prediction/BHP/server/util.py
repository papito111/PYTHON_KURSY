import pickle
import json
import numpy as np
__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations


def predict_price(location, m2,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = bath
    x[1] = bhk
    x[2] = m2
    if loc_index>= 0:
        x[loc_index] = 1
    return __model.predict([x])[0]


def load_safe_artificants():
    print("load files")
    global __data_columns
    global __locations
    global __model 
    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open('./artifacts/model.pickle','rb') as f:
        __model = pickle.load(f)
    print("loading done")


if __name__ =="__main__":
    load_safe_artificants()
    print(get_location_names)
    print(predict_price('1st Block Koramangala',100.2,3.0,4))