import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


# 1. data
data = {
    'Square_Feet': [1500, 2000, 1200, 1800, 2500, 3000, 3100, 2500, 2000, 2100],
    'Num_Bedrooms': [3, 4, 2, 3, 5, 5, 6, 6, 3, 2],
    'distance_town': [2.0, 2.5, 1.5, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0],
    'price': [300000, 450000, 250000, 400000, 600000, 60000, 70000, 80000, 40000, 35000]
}
df = pd.DataFrame(data)
print(df.head(),"\n")

# 2.features (X) and target (y) splitting
X = df.drop('price', axis=1)
y = df['price']

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#4.model selection
model = RandomForestRegressor(n_estimators=100, random_state=42)
# n_estimators: The number of trees in the forest.

#5.model training
model.fit(X_train, y_train)

# 6.predictions on the test set
y_pred = model.predict(X_test)

# 7. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2=r2_score(y_test,y_pred)
print(f"Mean Squared Error on test set: {mse:.4f}\n")
print(f"r2score :{r2}\n")


#new data prediction
house=[[1200,3,2],[2300,4,3]]
output=model.predict(house)
print("output is :\n",output,"\n\n")