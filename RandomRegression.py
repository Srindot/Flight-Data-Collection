import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
file_path = 'Mark3Data.csv'  # Update with your CSV file path
data = pd.read_csv(file_path, header=None)
data.drop([1])
# Assign column names
data.columns = ['Flapping Frequency', 'Airspeed', 'Angle Of Attack', 
                'Normalised Time', 'Lift', 'Induced Drag', 'Pitching Moment']

# Split the data into features and targets
X = data[['Flapping Frequency', 'Airspeed', 'Angle Of Attack', 'Normalised Time']]
y = data[['Lift', 'Induced Drag', 'Pitching Moment']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
print("Training is done")
# Evaluate the model
print("Model Performance:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))

# If you want to separate the predictions for each target
predicted_lift = y_pred[:, 0]
predicted_pitching_moment = y_pred[:, 1]
predicted_induced_drag = y_pred[:, 2]

# Example of evaluating each target separately
print("\nLift Model Performance:")
print("Mean Squared Error:", mean_squared_error(y_test['Lift'], predicted_lift))
print("R^2 Score:", r2_score(y_test['Lift'], predicted_lift))

print("\nPitching Moment Model Performance:")
print("Mean Squared Error:", mean_squared_error(y_test['Pitching Moment'], predicted_pitching_moment))
print("R^2 Score:", r2_score(y_test['Pitching Moment'], predicted_pitching_moment))

print("\nInduced Drag Model Performance:")
print("Mean Squared Error:", mean_squared_error(y_test['Induced Drag'], predicted_induced_drag))
print("R^2 Score:", r2_score(y_test['Induced Drag'], predicted_induced_drag))
