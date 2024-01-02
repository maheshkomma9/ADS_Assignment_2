#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:12:53 2023

@author: maheshroyal
"""
# import required libraries 
import pandas as pd
import matplotlib.pyplot as plt

# declaring the countries for comparision
countries=['India','China','Russia','Japan','United States','United Kingdom']

# define a function to read file
def read_file(filename):
    my_data=pd.read_excel(filename)

    print(my_data.describe())
    
    #selecting our required data
    req_data=my_data[(my_data['Country Name'].isin(countries))& 
                     (my_data['Year'].between(2014,2022))]
    print(req_data.head())
    
    for country in ['India','China','Russia','Japan','United States','United Kingdom']:
        country_data=req_data[req_data['Country Name']==country]
        
    #plotting the data of required data
        plt.plot(country_data['Year'],country_data['Literacy rate,youth total (% of people ages 15-24)']
                 ,label=country,linestyle='--')
        
        #labelling the data
        plt.legend()
        plt.xlabel('Year',color='teal',size=12)
        plt.ylabel('Literacy Rate',color='teal',size='12')
        plt.title('%Total youth agesg(15-24)',color='darkkhaki',size=15)
        
        # define the grid 
        plt.grid(True)
        plt.grid(which='major', color='#dddddd', linewidth=0.8)
        plt.grid(which='minor', color='#EEEEEE', linewidth=0.5)
        plt.minorticks_on()
        
filename='/Users/maheshroyal/Downloads/Book (11) copy.xlsx'
print(read_file(filename))
