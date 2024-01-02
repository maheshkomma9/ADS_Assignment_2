#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:54:22 2024

@author: maheshroyal
"""

# import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#defining the function 
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name)
    my_data_frame.set_index('Indicator Name', inplace=True)
    
    #retriving our required data
    req_data = my_data_frame.select_dtypes(include=['number'])
    print(req_data.describe())
    
    #plot the graph
    plt.figure(figsize=(12,8))
    sns.heatmap(req_data, annot = True, cmap = 'Paired',linewidths = 0.5)
    
    #adding labels to plot
    plt.title('Belgium')
    plt.show()
    
#declaring the file name
file_name = '/Users/maheshroyal/Downloads/Belgium.xlsx'
print(read_file(file_name))



