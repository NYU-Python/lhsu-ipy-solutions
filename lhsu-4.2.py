#!/usr/bin/env python

class PriceSummary():
    def __init__(self,filename):
        try:
            fh=open(filename,'a')
            self.handle = fh
            self.name = filename
        except IOError:
            return None
        
        
    #this function determines whether the input data is valid and also issues appropriate error messages
    #It takes in the 3 user input arguments and outputs a boolean value, indicating whether the data inputted is ok
    #valid summary types: max, min, avg, median, centered
    #days up to 251
    #tickers incl AAPL, FB, GOOG, LNKD, MSFT
    def is_valid(days,ticker):
        #probably preferable to import some other way, but not sure how so included the validations values here.
        valid_ticker = ["AAPL","FB","GOOG","LNKD","MSFT"] #list could also be built directly from file directory
        max_days = 251
        
        if ticker not in valid_ticker:
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
    
        #opening the tickerfile and making an empty list to fill later
        fh = open(ticker_file)
        relevant_prices = []
    
        #importing the entire list of ticker prices
        for line in fh.readlines()[1:number_rows]:
            columns = line.split(',')
            floatprice = float(columns[4])
            relevant_prices.append(floatprice)
    
        fh.close()
        return relevant_prices
    
    
    def maxprice(self, numdays):
        if not is_valid(numdays,self):
            return None
        else:
            list2calculate = get_data(numdays,self)
            maximumval = max(list2calculate)
            return maximumval
    
    
    def minprice(self, numdays)
        if not is_valid(numdays,self):
            return None
        else:
            list2calculate = get_data(numdays,self)
            minval = min(list2calculate)
            return minval
    
    def avg(self,numdays)
        if not is_valid(numdays,self):
            return None
        else:
            list2calculate = get_data(numdays,self)
            return (sum(price_list)/len(price_list))
    
    def median(self,numdays)
        if not is_valid(numdays,self):
            return None
        else:
            price_list = get_data(numdays,self)
            price_list.sort()
            list_length = len(price_list)
            if (list_length % 2) == 0: #if is even
                find_val1 = (list_length / 2) - 1
                find_val2 = find_val1
                return ((price_list[find_val1] + price_list[find_val2]) / 2)
            else: #otherwise it's odd
                find_val = (list_length / 2)
                return price_list[find_val]
    
    def centavg(self, numdays)
        if not is_valid(numdays,self):
            return None
        else:
            price_list = get_data(numdays,self)
            centered_list = list(set(price_list))
            return get_median(centered_list)
    
    
    
