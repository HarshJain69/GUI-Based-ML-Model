import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load and preprocess data
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
    df['region'] = df['region'].map({'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4})
    df['children'] = pd.to_numeric(df['children'], errors='coerce')
    df = df.dropna()  # Drop rows with NaN values
    return df

# Load and preprocess data
df = load_and_preprocess_data("insurance.csv")

# Define features (X) and target variable (y)
X = df.drop(['charges'], axis=1)
y = df['charges']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Linear Regression model
linreg = LinearRegression()
linreg.fit(X_train, y_train)
linreg_pred = linreg.predict(X_test)

# Train Random Forest Regression model
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train, y_train)
rf_pred = rf_regressor.predict(X_test)

# Train Support Vector Regression model
svr_regressor = SVR(kernel='linear')
svr_regressor.fit(X_train, y_train)
svr_pred = svr_regressor.predict(X_test)

# Calculate evaluation metrics for Linear Regression
linreg_mae = mean_absolute_error(y_test, linreg_pred)
linreg_mse = mean_squared_error(y_test, linreg_pred)
linreg_r2 = r2_score(y_test, linreg_pred)

# Calculate evaluation metrics for Random Forest Regression
rf_mae = mean_absolute_error(y_test, rf_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

# Calculate evaluation metrics for Support Vector Regression
svr_mae = mean_absolute_error(y_test, svr_pred)
svr_mse = mean_squared_error(y_test, svr_pred)
svr_r2 = r2_score(y_test, svr_pred)

# Display the comparison results
print("Comparison of Regression Models:")
print("Linear Regression:")
print("MAE:", linreg_mae)
print("MSE:", linreg_mse)
print("R²:", linreg_r2)
print("-----------------------------")
print("Random Forest Regression:")
print("MAE:", rf_mae)
print("MSE:", rf_mse)
print("R²:", rf_r2)
print("-----------------------------")
print("Support Vector Regression:")
print("MAE:", svr_mae)
print("MSE:", svr_mse)
print("R²:", svr_r2)