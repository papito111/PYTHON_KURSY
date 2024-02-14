from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/location')
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Acces','*')

    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_m2 = float(request.form['total_m2'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.predict_price(location,total_m2,bhk,bath)

    })

    return response

if __name__ =="__main__":
    print("starting home pred")
    util.load_safe_artificants()
    app.run()