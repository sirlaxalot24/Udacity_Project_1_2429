# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 08:43:09 2015

@author: jpaukov
"""

import numpy as np
import pandas
from sklearn.linear_model import SGDRegressor



def normalize_features(features):

    means = np.mean(features, axis=0)
    std_devs = np.std(features, axis=0)
    normalized_features = (features - means) / std_devs

    return means, std_devs, normalized_features

def recover_params(means, std_devs, norm_intercept, norm_params):

    intercept = norm_intercept - np.sum(means * norm_params / std_devs)
    params = norm_params / std_devs

    return intercept, params

def linear_regression(features, values):

    
    model = SGDRegressor(n_iter=1000)
    results = model.fit(features, values)
    intercept = results.intercept_
    params = results.coef_
    
    return intercept, params

def Rsquar(values, predictions):

    depMean = np.mean(values) 
    denom = np.sum((values - depMean) ** 2) 
    nomnom = np.sum((values - predictions) ** 2)
    r_squared = 1 - (nomnom / denom)
    
    return r_squared

"""                Ends helper funtions                """
"""                Ends helper funtions                """
"""                Ends helper funtions                """
"""                Ends helper funtions                """

dataframe = pandas.read_csv('C:\Users\jpaukov\Documents\Udacity\Project1\Udacity_Project_1_2429\Turnstile_weather_v2.csv')

features = dataframe[['rain', 'hour', 'weekday']]
dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
features = features.join(dummy_units)
    
values = dataframe['ENTRIESn_hourly']
    
features_array = features.values
values_array = values.values
    
means, std_devs, normalized_features_array = normalize_features(features_array)

norm_intercept, norm_params = linear_regression(normalized_features_array, values_array)
    
intercept, params = recover_params(means, std_devs, norm_intercept, norm_params)
    
predictions = intercept + np.dot(features_array, params)

r_squared = Rsquar(values, predictions)

print "R^2 - ", r_squared
print "Intercept - ", intercept
print "Params - ", params[0:4]













    