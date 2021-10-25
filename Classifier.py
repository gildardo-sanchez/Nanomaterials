#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:40:00 2021

@author: gildardo
"""

import pandas as pd
import numpy as np


# Confusion matrix 
def accuracy(confusion_matrix):
   diagonal_sum = confusion_matrix.trace()
   sum_of_all_elements = confusion_matrix.sum()
   return diagonal_sum / sum_of_all_elements


# Load data. The original dataset includes names in first row
dataset = pd.read_csv("data11tumors2.csv")

# Separate the class from the attributes
target = pd.DataFrame(dataset, columns= ['Class'])

#print (target)

attributes= dataset.loc[ : , dataset.columns != 'Class']
#print(attributes)

#Splitting the dataset into  training and validation sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(
    attributes,target,test_size=0.33, random_state=50)

#print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Train one model with raw data to establish a reference.
# In this case, we will train a MLP
from sklearn.neural_network import MLPClassifier

#Initializing the MLPClassifier
classifier = MLPClassifier(hidden_layer_sizes=(100,50,10), max_iter=1000,
                           activation = 'relu',solver='adam',random_state=1)

#Fitting the training data to the network
classifier.fit(X_train, y_train.values.ravel())

#Predicting y for X_val
y_pred = classifier.predict(X_test)

#Importing Confusion Matrix
from sklearn.metrics import confusion_matrix
#Comparing the predictions against the actual observations in y_test
cm = confusion_matrix(y_pred, y_test)

#Printing the accuracy
print("Accuracy of MLPClassifier with raw data: ", accuracy(cm))


# Up to here, we are working on the original space (n dimensions)
# We will reduce the dimensions by computing PCA and take m dimensions
# where m<n


# Principal Component Analysis for dimension reduction

from sklearn.decomposition import PCA
pca = PCA(0.20)

# Fit PCA on training set
pca.fit(X_train)

# We need to transform the original split sets into the new subspace
# given by PCA. This is done for both X_train and X_test
# Apply the mapping (transform) to both the training set and the test set.
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

#print(pca.n_components_)

print("shape of X_pca", X_train_pca.shape, X_test_pca.shape)
expl = pca.explained_variance_ratio_
print(expl)


print('suma:',sum(expl[0:20]))


#Initializing the MLPClassifier
classifier_pca = MLPClassifier(hidden_layer_sizes=(500,100,50), max_iter=1000,
                           activation = 'relu',solver='adam',random_state=1)

#Fitting the training data to the network
classifier_pca.fit(X_train_pca, y_train.values.ravel())

#Predicting y for X_val
y_pred_pca = classifier_pca.predict(X_test_pca)

#Importing Confusion Matrix
from sklearn.metrics import confusion_matrix
#Comparing the predictions against the actual observations in y_test
cm = confusion_matrix(y_pred_pca, y_test)

#Printing the accuracy
print("Accuracy of MLPClassifier with PCA data: ", accuracy(cm))




