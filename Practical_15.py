# Use some function for regularization of dataset based on problem 14

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('student_data.csv')

df['gender'] = df['gender'].map({'F':0, 'M':1})

X = df[['gender', 'height', 'weight', 'math_score', 'reading_score', 'writing_score']] 
y = df['activity'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg = LogisticRegression(penalty='l2', C=0.1)

log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print('Accuracy score:', acc)
print('Confusion matrix:\n', cm)
print('Classification report:\n', cr)
