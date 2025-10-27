"""Main Flask application for car price prediction."""
import os
import sys
import pickle
import json
import numpy as np
from flask import Flask, render_template, redirect, url_for, request, jsonify
from lightgbm import LGBMRegressor

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from transformation_functions import (
    Car_age, Old_or_New, Car_Usage_level, State_level, City_level
)

app = Flask(__name__)

# Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'data')
MODELS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'models')

price = None

# Load JSON data files
with open(os.path.join(DATA_DIR, 'feature-transformation-data.json')) as f:
    maps_dict = json.load(f)

with open(os.path.join(DATA_DIR, 'models_to_makes.json')) as f:
    models_to_makes = json.load(f)

with open(os.path.join(DATA_DIR, 'cities_to_states.json')) as f:
    cities_to_states = json.load(f)

# Prepare dropdown options
states = sorted(list(cities_to_states.keys()))
makes = sorted(list(models_to_makes.keys()))
cities = sorted(list(cities_to_states[states[0]]))
models = sorted(list(models_to_makes[makes[0]]))

# Load ML model
ml_model = pickle.load(open(os.path.join(MODELS_DIR, 'lgb'), 'rb'))


def transform_features(city, state, year, mileage, make, model):
    """Transform input features for model prediction."""
    features = {}
    encoded_city = maps_dict['city-value-count'][city]
    encoded_state = maps_dict['state-value-count'][state]

    features['MFG_YEAR'] = year
    features['CAR_AGE'] = Car_age(year)
    features['MILEAGE'] = mileage
    features['CAR_DRIVEN_PER_YEAR'] = mileage / features['CAR_AGE'] if features['CAR_AGE'] > 0 else 0
    features['STATE'] = state
    features['MAKE'] = make
    features['MODEL'] = model
    features['CITY'] = city
    features['STATE_IMPORTANCE'] = State_level(encoded_state)
    features['CITY_IMPORTANCE'] = City_level(encoded_city)
    features['OLD_OR_NEW'] = Old_or_New(features['CAR_AGE'])
    features['CAR_USAGE_LEVEL'] = Car_Usage_level(features['CAR_DRIVEN_PER_YEAR'])

    for column in maps_dict['categorical-cols']:
        features[f'{column}_ENCODED'] = maps_dict[f"{column}-avg-price"][features[column]]
        features[f'{column}_ENCODED'] = np.log(features[f'{column}_ENCODED'])

    data_sample = []
    for column in maps_dict['final-data-columns']:
        if (column != 'PRICE') and (column != 'ID'):
            data_sample.append(features[column])

    return data_sample


@app.route('/')
def index():
    """Home page with car price prediction form."""
    title = "Know Your Car"
    return render_template('index.html', titel=title, price=price, states=states,
                          cities=cities, makes=makes, models=models)


@app.route('/getprice', methods=['POST'])
def getPrice():
    """Process form submission and predict car price."""
    try:
        city = request.form.get('city-name')
        state = request.form.get('state-name')
        make = request.form.get('make-name')
        model = request.form.get('model-name')
        purchase_year = int(request.form.get('purchase-year'))
        mileage = int(request.form.get('mileage'))

        sample = transform_features(
            city=city, state=state, year=purchase_year,
            mileage=mileage, make=make, model=model
        )

        global price
        price = np.round(ml_model.predict(np.array(sample).reshape(1, -1))[0], 2)

    except (ValueError, KeyError) as e:
        print(f"Error processing request: {e}")

    return redirect(url_for('index'))


@app.route('/about-us')
def about():
    """About us page."""
    return render_template("about.html")


@app.route('/contact-us')
def contact():
    """Contact us page."""
    return render_template("contact_us.html")


@app.route('/login')
def login():
    """Login page."""
    return render_template("Sign_in.html")


@app.route('/register')
def register():
    """Registration page."""
    return render_template("sign_up.html")


@app.route('/city/<state>')
def city(state):
    """API endpoint to get cities for a given state."""
    return jsonify({'cities': sorted(list(cities_to_states.get(state, [])))})


@app.route('/model/<make>')
def model(make):
    """API endpoint to get models for a given make."""
    return jsonify({'models': sorted(list(models_to_makes.get(make, [])))})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
