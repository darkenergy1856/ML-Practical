# Implement Linear Regression problem. For example, based on a dataset comprising of 
# existing set of prices and area/size of the houses, predict the estimated price of a given house.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("house_prices.csv")

X = df["area"].values 
y = df["price"].values 

plt.scatter(X, y, color="blue")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

def hypothesis(theta0, theta1, x):
  return theta0 + theta1 * x

def cost(theta0, theta1, X, y):
  m = len(X) 
  total_cost = 0 
  for i in range(m): 
    total_cost += (hypothesis(theta0, theta1, X[i]) - y[i]) ** 2 
  return total_cost / (2 * m) 

def gradient_descent(theta0, theta1, X, y, alpha, iterations):
  m = len(X) 
  for i in range(iterations): 
    
    grad0 = 0 
    grad1 = 0
    for j in range(m): 
      
      grad0 += (hypothesis(theta0, theta1, X[j]) - y[j])
      grad1 += (hypothesis(theta0, theta1, X[j]) - y[j]) * X[j]
    
    theta0 = theta0 - alpha * grad0 / m
    theta1 = theta1 - alpha * grad1 / m
  return theta0, theta1 

theta0 = 0 
theta1 = 0 
alpha = 0.00001

iterations = 1000

theta0, theta1 = gradient_descent(theta0, theta1, X, y, alpha, iterations)

print("The optimal parameters are:")
print("theta0 =", theta0)
print("theta1 =", theta1)

plt.scatter(X, y, color="blue")
plt.plot(X, hypothesis(theta0, theta1, X), color="red")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

def predict_price(area):
  return hypothesis(theta0, theta1, area)

print("The predicted price for a house with area 120 is:", predict_price(120))
print("The predicted price for a house with area 150 is:", predict_price(150))
