# Use some function for neural networks, like Stochastic Gradient Descent or backpropagation- algorithm to predict the value of a variable based on the dataset of problem 14

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt 

df = pd.read_csv('student_data.csv')

df['gender'] = df['gender'].map({'F':0, 'M':1})

X = df[['gender', 'height', 'weight', 'math_score', 'reading_score', 'writing_score']] 
y = df['activity'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()

model.add(Dense(8, input_dim=6, activation='sigmoid'))

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0) 

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['accuracy'], label='accuracy')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend()
plt.show()

_, acc = model.evaluate(X_test, y_test)

y_pred = model.predict(X_test)
y_pred = np.round(y_pred)

cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print('Confusion matrix:\n', cm) 
print('Classification report:\n', cr) 
