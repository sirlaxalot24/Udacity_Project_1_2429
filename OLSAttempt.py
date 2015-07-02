# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 16:35:56 2015

@author: jpaukov
"""

import numpy as np
import pandas
import statsmodels.api as sm

dataframe = pandas.read_csv('C:\Users\jpaukov\Documents\Udacity\Project1\Udacity_Project_1_2429\Turnstile_weather_v2.csv')

def linear_regression(features, values):
    
    
    features = sm.add_constant(features)
    
    model = sm.OLS(values, features)
    model = model.fit()
    intercept = model.params[0]
    params = model.params[1:]
    
    return intercept, params
    
def Rsquar(depMean, predictions):

    depVar = dataframe['ENTRIESn_hourly'] 
    denom = np.sum((depVar - depMean) ** 2) 
    nomnom = np.sum((depVar - predictions) ** 2)
    r_squared = 1 - (nomnom / denom)
    
    return r_squared

features = dataframe[['rain', 'hour', 'meantempi', 'precipi' ]]
dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
dummy_units2 = pandas.get_dummies(dataframe['conds'], prefix='conds')
features = features.join(dummy_units)
features = features.join(dummy_units2)

values = dataframe['ENTRIESn_hourly']
   
depMean = np.mean(dataframe['ENTRIESn_hourly'])

intercept, params = linear_regression(features, values)

predictions = intercept + np.dot(features, params)

r_squared = Rsquar(depMean, predictions)


print r_squared 