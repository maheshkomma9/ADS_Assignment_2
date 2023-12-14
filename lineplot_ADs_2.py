#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:20:39 2023

@author: maheshroyal
"""

import pandas as pd
import matplotlib.pyplot as plt
countries=['India','China','Russia','Japan','United States','United Kingdom']
def read_file(filename):
    my_data=pd.read_excel(filename)

    print(my_data.describe())
    Data_req=my_data[(my_data['Country Name'].isin(['India','China','Russia','Japan','United States','United Kingdom']))& 
                     (my_data['Year'].between(2014,2022))]
    print(Data_req.head())
    def indicator_data_to_plot(indicator_name):
        for country in ['India','China','Russia','Japan','United States','United Kingdom']:
            Final_data=Data_req[Data_req['Country Name']==country]
        
       
            
            plt.plot(Final_data['Year'],Final_data[indicator_name]
                 ,label=country,linestyle='--')
        
            plt.legend()
            plt.xlabel('Year',color='teal',size=12)
            plt.ylabel('Population in millions',color='teal',size='12')
            plt.title('%Total youth ages(15-60)',color='darkkhaki',size=15)
        
            plt.grid(True)
            plt.grid(which='major', color='#dddddd', linewidth=0.8)
            plt.grid(which='minor', color='#EEEEEE', linewidth=0.5)
            plt.minorticks_on()
    indicator_name=('Total Population of ages(15-60)')
    print(indicator_data_to_plot(indicator_name))
filename='/Users/maheshroyal/Downloads/Book (11) copy 3.xlsx'
print(read_file(filename))