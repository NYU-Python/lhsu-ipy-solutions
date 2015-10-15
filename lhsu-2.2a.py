#!/usr/bin/env python

#Bit.ly problem

# ------------------------------------------
# FUNCTIONS
# ------------------------------------------

# this function intakes a .tsv with user data and an index number to search in file
# outputs a set of cities
def column_set(filename,column_index):
    outputset = set()
    fh = open(filename)
    for line in fh.readlines()[1:]:
        eachline = line.split('\t')
        outputset.add(eachline[column_index])
    return outputset


# this function intakes an unordered set of strings and sorts it
# alphabetically, outputting an alphabetized set
def alphabetize(unordered_set):
    for item in unordered_set:
        item.upper()
    ordered_set = sorted(unordered_set)
    return ordered_set
    
# this function intakes a .tsv with an index number to build from
# it outputs a dictionary of with values that indicate total count for each given key
def build_dict(filename, column_index)
    outputdict = {}
    fh = open(filename)
    for line in fh.readlines()[1:]:
        eachline = line.split('\t')
        if eachline[column_index] is in outputdict:
            outputdict[eachline[column_index]] = outputdict[eachline[column_index]]+1
        else:
            outputdict[eachline[column_index]] = 1
    return output dict
    
# this function intakes a dictionary with all integer values and outputs a sorted list of the associated keys
def get_list(mydict)
    sorted_list = sorted(mydict,key = mydict.get)
    return sorted_list
    
# ------------------------------------------
# SCRIPT for part a
# ------------------------------------------

#Unique cities
fileinput = str(raw_input('What file would you like me to look at? '))

citycolumnindex = 3

cityset = alphabetize(column_set(fileinput,citycolumnindex))

print cityset
