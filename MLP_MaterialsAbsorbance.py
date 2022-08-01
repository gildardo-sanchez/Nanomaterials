#!/usr/bin/env python
# coding: utf-8

# # MLP regression for absorbance computation
# 
# This code will read the csv file with the data for the computation of a model to
# predict absorbance.
# 
# It will use a multi-layer perceptron

# # Step 1 - Loading the Required Libraries and Modules

# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score


# # Step 2 - Reading the Data and Performing Basic Data Checks

# 

# Load data. The original dataset includes names in first row
#dataset = pd.read_csv("dataframe_ZnER_EC_clean.csv")
dataset = pd.read_csv("database_EC_norm_trans.csv")

# Separate the class from the attributes
target = pd.DataFrame(dataset, columns= ['Abs'])

print (target)

attributes= dataset.loc[ : , dataset.columns != 'Abs']
print(attributes)


# # Split dataset


#Splitting the dataset into  training and validation sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(
    attributes,target,test_size=0.33, random_state=50)

#print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# # Train (fit) an MLP
# Train an MLP as a regression model. In this case, we will make a three layers model. First with 100 neurons, second with 50 and last with 10. Relu activation, and Solver Adam Once the model is trained, we ask it to predict values and store them on y_pred


# Train one model with raw data to establish a reference.
# In this case, we will train a MLP
from sklearn.neural_network import MLPRegressor

#Initializing the MLPRegressor
regr = MLPRegressor(hidden_layer_sizes=(500,100,40), max_iter=10000,
                           activation = 'relu',solver='lbfgs',random_state=1)

#Fitting the training data to the network
regr.fit(X_train, y_train.values.ravel())

#Predicting y for X_val
y_pred = regr.predict(X_test)


# # Compute accuracy. 
# The score by default is r^2.
# 
# R^2(coefficient of determination) regression score function.
# 
# Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of y, disregarding the input features, would get a 
# R^2 score of 0.0.

regr.score(X_test, y_test)


# Now use a linear regression


from sklearn.linear_model import LinearRegression

model = LinearRegression() 

model.fit(X_train, y_train)

# Predicting y for X_val
y_pred2= model.predict(X_test)



from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
