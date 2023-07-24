import pickle

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('newPakwheeldst.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    
    print(car_models)
    companies.insert(0, 'Select Company')

    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')

    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = request.form.get('kilo_driven')
    x = ' '
    print(x.join(car_model.split()[1:-1]))
    if fuel_type=="Diesel":
        fuel_type = 1
    else:
        fuel_type = 0

    prediction = model.predict(pd.DataFrame(columns=['model', 'company', 'year', 'kms_driven', 'fuel_type'],
                                            data=np.array([x.join(car_model.split()[1:]), company, year, driven, fuel_type]).reshape(1, 5)))
    
    #prediction = model.predict([[x,comapany,]])
    print(prediction)

    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(port=50001,debug=True)
