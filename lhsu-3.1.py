#!/usr/bin/env python

import argparse
import os
import sys

# FUNCTIONS
# ---------------------------------

# This function intakes a directory name and outputs a dictionary of dictionary of attributes about each file in the directory
# The attributes are: bare filename, size, and last modification time
def file_attributes(mypath):
    dictodir={}
    file_list = os.listdir(mypath)
    for item in file_list[1:]:
        dictodir[item] = {'bare filename':os.path.basename(item), 'size':os.path.getsize(mypath+"/"+item), 'last mod time':os.path.getmtime(mypath+"/"+item)}
    return dictodir
    
    
# This function intakes a dictionary of dictionaries, inner attribute to sort by, direction of sort (string), and qty of
# entries to return. It returns an ordered list of the attributes based on the inputs
def dict_sort(mydict, sort_by, direction, how_many):
    if direction == 'ascending':
        sort_dir = True
    else:
        sort_dir = False
    sortedlist = sorted(mydict,key=lambda x: mydict.get(x).get(sort_by) , reverse=sort_dir)
    indexcorr = how_many-1
    shortlist = sortedlist[0:indexcorr]
    return shortlist

# This function intakes a list and a dictionary, and builds a new dictionary only using values from the
# list, pulling values from the dictionary
def list_to_dict(mylist,mydict):
    newdict = {}
    for el in mylist:
        newdict[el] = mydict[el]
    return newdict

# SCRIPT
# ----------------------------------

# argparse set-up
parser = argparse.ArgumentParser(description='Takes in 4 arguments: directory location, sort criteria, # results, sort direction')

parser.add_argument('--dir',required=True, help='which directory should I look in')
parser.add_argument('--by',choices=('size','mtime','name'),required=True, help='what attribute should I sort by - size, mtime, or name')
parser.add_argument('--results',type=int,required=True, help='how many results I should display')
parser.add_argument('--direction',choices=('ascending','descending'),required=True, help='how should I sort - ascending or descending')

args = parser.parse_args()
dictodir = {}

sortby = args.by
directory = args.dir
direction = args.direction
howmany = args.results

try:
    attribute_dict = file_attributes(directory)
    list_keys = dict_sort(attribute_dict,sortby,direction,howmany)
    attribute_dictshorter = list_to_dict(list_keys,attribute_dict)
    print attribute_dictshorter
except OSError:
    print ('You should try again; your directory was fake.')
    sys.exit()
    
    
    
    
    
