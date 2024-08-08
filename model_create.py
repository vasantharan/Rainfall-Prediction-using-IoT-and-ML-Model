import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the dataset
file_path = './Rainfall_data.csv'
data = pd.read_csv(file_path)

def calculate_absolute_humidity(temp, rh):
    return (6.112 * np.exp((17.67 * temp) / (temp + 243.5)) * rh * 2.1674) / (temp + 273.15)

data['Actual_Humidity'] = calculate_absolute_humidity(data['Temperature'], data['Relative Humidity'])

data = data.drop(columns=['Specific Humidity', 'Relative Humidity'])

X = data.drop(columns=['Precipitation'])
y = data['Precipitation']

scaler = StandardScaler()
X = scaler.fit_transform(X)

model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X, y)

joblib.dump(model, './prediction_model.joblib')
print('Save successfully')