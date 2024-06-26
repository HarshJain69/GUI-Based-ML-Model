

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def load_and_preprocess_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Feature engineering
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
    df['region'] = df['region'].map({'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4})

    # Handle non-numeric values in 'children' column
    df['children'] = pd.to_numeric(df['children'], errors='coerce')
    df = df.dropna()  # Drop rows with NaN values

    return df

def train_linear_regression(X_train, y_train):
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    return linreg

def input_new_customer(unit_option, bmi_option):
    print("\n--- Input details for the new customer ---")

    # Input height and weight units
    if unit_option == "kg/m":
        weight_unit, height_unit = "kilograms", "meters"
    else:
        weight_unit, height_unit = "pounds", "inches"

    # Input BMI or calculate it based on weight and height
    if bmi_option == "yes":
        bmi = float(input("Enter customer's BMI: "))
    else:
        weight = float(input(f"Enter customer's weight in {weight_unit}: "))
        height = float(input(f"Enter customer's height in {height_unit}: "))
        bmi = weight / (height ** 2)

    age = int(input("Enter customer's age: "))
    children = int(input("Enter the number of children: "))
    smoker = int(input("Is the customer a smoker? (1 for Yes, 0 for No): "))
    sex = int(input("Is the customer male? (0 for Yes, 1 for No): "))
    region = int(input("Enter customer's region (1: southwest, 2: southeast, 3: northwest, 4: northeast): "))

    return {'age': age, 'bmi': bmi, 'children': children, 'smoker': smoker, 'region': region, 'sex': sex}


def predict_for_new_customers(linreg, new_customers_df, X_train_columns):
    new_customer_df = new_customers_df.reindex(columns=X_train_columns, fill_value=0)
    cost_pred = linreg.predict(new_customer_df)
    if cost_pred < 0:
        cost_pred *= -1  # Make the prediction positive
    return cost_pred


def display_results(cost_pred, currency_option):
    # Displaying the cost in the chosen currency
    if currency_option != "USD":
        cost_pred_inr = cost_pred * 74.5  # Assuming an exchange rate of 1 USD = 74.5 INR
        print("\nEstimated medical insurance cost for the new customer:")
        print(f"₹{cost_pred_inr[0]:.2f}")
    else:
        print("\nEstimated medical insurance cost for the new customer:")
        print(f"${cost_pred[0]:.2f}")

def main():
    df = load_and_preprocess_data("insurance.csv")

    X = df.drop(['charges'], axis=1)
    y = df['charges']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    linreg = train_linear_regression(X_train, y_train)

    unit_option = input("Choose input units for weight and height (kg/m or lbs/inches): ").lower()

    currency_option = input("Choose the currency for displaying cost (INR or other): ").upper()

    bmi_option = input("Do you want to input BMI directly? (yes/no): ").lower()

    new_customer_data = input_new_customer(unit_option, bmi_option)

    new_customer_df = pd.DataFrame([new_customer_data])

    X_train_columns = list(X_train.columns)
    cost_pred = predict_for_new_customers(linreg, new_customer_df, X_train_columns)

    display_results(cost_pred, currency_option)

if __name__ == "__main__":
    main()
