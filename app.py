from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the insurance dataset
df = pd.read_csv('insurance.csv')

# Feature engineering
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
df['sex'] = df['sex'].map({'female': 1, 'male': 0})
df['region'] = df['region'].map({'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4})

# Define features and target variable
X = df[['age', 'bmi', 'children', 'smoker', 'sex', 'region']]
y = df['charges']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Define route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        sex = int(request.form['sex'])
        region = int(request.form['region'])

        # Make prediction
        prediction = model.predict([[age, bmi, children, smoker, sex, region]])

        # Return prediction as JSON response
        print(prediction)
        return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
