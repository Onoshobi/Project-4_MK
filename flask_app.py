from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Let's load(unpickle) the model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the home route for displaying the form
@app.route('/')
def index():
    
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    #in this format ['man', 'near_location', 'partner', 'promo_friends', 'phone', 'group_visits', 'age', 'charges_for_services', 'month_to_end', 'lifetime', 'frequency_total']
    data = [
        request.form['gender'],
        request.form['near_location'],
        request.form['partner'],
        request.form['promo_friends'],
        1 if(request.form['phone'])==10 else 0,
        request.form['group_visits'],
        request.form['age'],
        146.943, #took average charge from dataset using excel(charges_for_services) : Avg_additional_charges_total
        4.32, #took average month to end from dataset using excel(month_to_end_contract) : Avg_month_to_end,
        3.72,#request.form['lifetime'] : took average lifetime from dataset using excel(lifetime) : lifetime,
        int(request.form['avg_class_frequency_current_week']),
    ]
    

    
    # Convert data to appropriate format
    data = np.array(data).reshape(1, -1).astype(float)

    # Make prediction
    prediction = model.predict_proba(data)[0][0] # 0 for no churn, 1 for churn

    # Show result based on prediction
    result = 'Churn' if prediction == 1 else 'No Churn'

    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == '__main__':
    app.run(debug=True)
