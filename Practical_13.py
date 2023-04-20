# Based on multiple features/variables perform Linear Regression. For example, based on a
# number of additional features like number of bedrooms, servant room, number of balconies,
# number of houses of years a house has been built – predict the price of a house.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_prices_multi.csv")

X = df[["area", "bedrooms", "servant_room", "balconies", "age"]].values 
y = df["price"].values 

model = LinearRegression()

model.fit(X, y)

print("The coefficients are:", model.coef_)
print("The intercept is:", model.intercept_)

def predict_price(area, bedrooms, servant_room, balconies, age):
  return model.predict([[area, bedrooms, servant_room, balconies, age]])[0]

print("The predicted price for a house with area 120, 2 bedrooms, 1 servant room, 1 balcony and 10 years old is:", predict_price(120, 2, 1, 1, 10))
print("The predicted price for a house with area 150, 3 bedrooms, 0 servant room, 2 balconies and 5 years old is:", predict_price(150, 3, 0, 2, 5))
