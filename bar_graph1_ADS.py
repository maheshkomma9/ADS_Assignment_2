#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:27:08 2023

@author: maheshroyal
"""
#import required libraries
import pandas as pd
import matplotlib.pyplot as plt

#declaring required countries
countries = ['India','United States','Russia','Germany','Brazil','Canada','Japan','Canada','United Kingdom']

# defining the function to read file
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name, skiprows = 3)
    print(my_data_frame)
    
    #retriving required data of years
    req_years_df = my_data_frame.iloc[:, -8:]
    print(req_years_df.head())
    
    #retrive selected data of countries and years
    my_req_data_frame = my_data_frame[my_data_frame['Country Name'].isin(countries)
        ][['Country Name','2015','2016','2017','2018','2019','2020','2021','2022']]
    print(my_req_data_frame.describe())
    
    #plot the graph
    my_req_data_frame.plot.bar(x='Country Name',figsize=(12,8))
    
    #labelling the graph
    plt.title('Share of youth not in Education,Training',color='cadetblue',fontsize=(25))
    plt.xlabel('Country Name',fontsize=(15),color='Grey')
    plt.ylabel('ILO Estimate Readings',fontsize=(15))
    
# declaring file name
file_name='/Users/maheshroyal/Downloads/API_SL.UEM.NEET.MA.ZS_DS2_en_excel_v2_6231813.xls'
print(read_file(file_name))
    
