from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))
car_data = pd.read_csv('Cleaned_csv_file.csv')

@app.route('/')
def retrive_categories():
    company = sorted(car_data['company'].unique())
    car_models = sorted(car_data['name'].unique())
    car_models.insert(0, "Select the model")
    purchase_year = sorted (car_data['year'].unique(), reverse=True)
    fuel_type = car_data['fuel_type'].unique()
    return render_template("index.html", companies=company, car_models=car_models, purchase_years = purchase_year,fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model') 
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]], columns=['name', 'company', 'year','kms_driven', 'fuel_type']))
    print(prediction )
    return str(prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
 
 