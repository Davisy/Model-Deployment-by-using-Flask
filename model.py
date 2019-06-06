# import packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import r2_score

#load dataset
dataset = pd.read_csv('data/salary_data.csv')

# split data into features and target
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#split the data into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05, random_state = 0)

# create a model
regressor = LinearRegression()

#train the model
regressor.fit(X_train, y_train)

#perform prediction
y_pred = regressor.predict(X_test)

# you can check the peformance of the model from the following code
#print("R2 score: {}".format(r2_score(y_test,y_pred)))

#save the trained model
pickle.dump(regressor, open('models/regressor.pkl','wb'))
