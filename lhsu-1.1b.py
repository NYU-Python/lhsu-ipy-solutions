#!/usr/bin/env python

import csv
import pandas as pd

valid_summary = ["maximum","minimum","average","median","centered"]
valid_ticker = ["AAPL","FB","GOOG","LNKD","MSFT"] #list could also be built directly from file directory
max_days = 251

#*******************
#FUNCTIONS IN THIS SECTION
#*******************


#this function determines whether the input data is valid and also issues appropriate error messages
#It takes in the 3 user input arguments and outputs a boolean value, indicating whether the data inputted is ok
#valid summary types: max, min, avg, median, centered
#days up to 251
#tickers incl AAPL, FB, GOOG, LNKD, MSFT
def is_valid(summary,days,ticker):
    if summary not in valid_summary:
        print ('Try again, your input for summary type was invalid. Valid values for the summary type are:')
        print valid_summary
        return False
    elif ticker not in valid_ticker:
        print ('Try again, I do not have a record of that ticker. I know about these tickers: ')
        print valid_ticker
        return False
    elif days > max_days:
        print ('Try again, I do not have that much data. I have up to ' + str(max_days) + ' days of price data.')
        return False
    else:
        return True
    

#this function retrieves the appropriate number of data points as requested
#it takes in a number (days) and a ticker string, and outputs a list of variable length
#close price is in column 5
def get_data(days,ticker):
    number_rows = int(days) #ensures that the days input will be converted to an int if it's not
    ticker_file = ticker + '.csv' #converts ticker into a file-name by appending .csv
    #with open (ticker_file,'rb') as infile:
    #    sheet = csv.reader(infile,dialect=csv.excel_tab,delimiter=",")
    
    #opening the tickerfile and making an empty list to fill later
    fh = open(ticker_file)
    relevant_prices = []
    
    #importing the entire list of ticker prices
    for line in fh.readlines()[1:number_rows]:
        columns = line.split(',')
        floatprice = float(columns[4])
        relevant_prices.append(floatprice)
    
    fh.close()
    
    #importing the entire ticker file into my program using pandas NOT USING
    #stock_data = pd.read_csv(ticker_file)
    
    #making a list of just the closing prices NOT USING
    #closing_prices = stock_data.Close
    
    #making a list of the closing prices for the applicable date range NOT USING
    #relevant_prices = closing_prices[1:number_rows]
    
    return relevant_prices
        
    
#this function intakes a list and outputs the median of the list
def get_median(price_list):
    price_list.sort()
    list_length = len(price_list)
    if (list_length % 2) == 0: #if is even
        find_val1 = (list_length / 2) - 1
        find_val2 = find_val1
        return ((price_list[find_val1] + price_list[find_val2]) / 2)
    else: #otherwise it's odd
        find_val = (list_length / 2)
        return price_list[find_val]

#this function intakes a list and outputs the centered median of the list
def get_centered(price_list):
    centered_list = list(set(price_list))
    return get_median(centered_list)
    
#this function intakes a list and outputs the maximum of the list
def get_max(price_list):
    ordered_set = list(set(price_list))
    return ordered_set[len(ordered_set)-1]

#this function intakes a list and outputs the minimum of the list
def get_min(price_list):
    ordered_set = list(set(price_list))
    return ordered_set[0]

#this function intakes a list and outputs the arithmetic average of the list
def get_average(price_list):
    return (sum(price_list)/len(price_list))
    
#********
#SCRIPT STARTS HERE
#********


#naming the variables to lead the if statements
maximum = 'maximum'
minimum = 'minimum'
average = 'average'
median = 'median'
centered = 'centered'

#this loop will keep going until we get the correct format of input data
while True:
    print('Options for summary include: ')
    print(valid_summary)
    summarytype = raw_input('What type of summary would you like?')
    tradingdays = raw_input('How many trading days would you like me to consider? I have 251 days worth of data. ')
    print('Options for tickers include: ')
    print(valid_ticker)
    tickertoquery = raw_input('What ticker would you like to query for?')
    tickertoquery = tickertoquery.upper()
    if is_valid(summarytype,tradingdays,tickertoquery) is True:
        break
    
list2calculate = get_data(tradingdays,tickertoquery)

if summarytype == maximum:
    answer = get_max(list2calculate)
elif summarytype == minimum:
    answer = get_min(list2calculate)
elif summarytype == average:
    answer = get_average(list2calculate)
elif summarytype == median:
    answer = get_median(list2calculate)
elif summarytype == centered:
    answer = get_centered(list2calculate)

print tickertoquery
print answer
