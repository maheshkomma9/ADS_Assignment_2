#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:13:33 2023

@author: maheshroyal
"""
#import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# declaring countries need to plot
countries = ['India','United States','Russia','China','Brazil','Canada','Japan','Canada','United Kingdom']

# defining the function to read file
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name, skiprows = 3)
    print(my_data_frame)
    
    # retrive specific set of year from data frame
    req_years_df = my_data_frame.iloc[:, -8:]
    print(req_years_df.head())
    
    #retrive specific data to plot from data set
    my_req_data_frame = my_data_frame[my_data_frame['Country Name'].isin(countries)
        ][['Country Name','2015','2016','2017','2018','2019','2020','2021','2022']]
    print(my_req_data_frame.describe())
    
    #plot the graph
    my_req_data_frame.plot.bar(x='Country Name',figsize=(12,8))
    
    #labelling the data
    plt.title('Unemployment, total (% of total labor force',color='cadetblue',fontsize=(25))
    plt.xlabel('Country Name',fontsize=(15),color='Grey')
    plt.ylabel('ILO Estimate Readings',fontsize=(15))
    
# declaring the file name
file_name='/Users/maheshroyal/Downloads/API_SL.UEM.TOTL.ZS_DS2_en_excel_v2_6224948.xls'
print(read_file(file_name))
    

