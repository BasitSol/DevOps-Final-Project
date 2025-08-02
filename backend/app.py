from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import traceback

app = Flask(__name__)
CORS(app)
#Now this is the Final 
#This is just comment for the pipeline test
# Load your trained model
try:
    model = joblib.load('Cancer_Detection.pkl')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    print(traceback.format_exc())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Received data:", request.json)
        
        data = request.json
        required_fields = ['age', 'gender', 'bmi', 'smoking', 'geneticRisk', 
                         'physicalActivity', 'alcoholIntake', 'cancerHistory']
        
        # Check for missing fields
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400

        # Convert data to correct format with matching column names
        input_data = pd.DataFrame([{
            'Age': data['age'],
            'Gender': data['gender'],
            'BMI': data['bmi'],
            'Smoking': data['smoking'],
            'GeneticRisk': data['geneticRisk'],
            'PhysicalActivity': data['physicalActivity'],
            'AlcoholIntake': data['alcoholIntake'],
            'CancerHistory': data['cancerHistory']
        }])

        print("Processed input data:", input_data)
        
        prediction = model.predict(input_data)
        print("Prediction result:", prediction)
        
        return jsonify({'prediction': int(prediction[0])})
    
    except Exception as e:
        print("Error occurred:", str(e))
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Flask in debug mode should NOT be used in production.
    # For development, 0.0.0.0 allows access from outside the container's localhost.
    app.run(debug=True, host='0.0.0.0', port=5000)
