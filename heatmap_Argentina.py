#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:30:29 2024

@author: maheshroyal
"""

#import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#defining the function 
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name)
    my_data_frame.set_index('Indicator Name', inplace=True)
    
    #retriving the required data
    req_data = my_data_frame.select_dtypes(include=['number'])
    print(req_data.describe())
    
    #plot the graph
    plt.figure(figsize=(12,8))
    sns.heatmap(req_data, annot = True, cmap = 'coolwarm',linewidths = 0.5)
    
    #labelling the data
    plt.title('Argentina')
    plt.show()
    
#declaring the file name
file_name = '/Users/maheshroyal/Downloads/Argentina.xlsx'
print(read_file(file_name))



