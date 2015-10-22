#!/usr/bin/env python

import sys

# CONFIGURATION VALUES
# -----------------------------
platforms = ('Android','Blackberry','Windows NT','iPad', 'iPhone', 'iPad', 'iPod', 'Linux', 'Macintosh', 'PLAYSTATION 3', 'PSP')


# FUNCTIONS
# -----------------------------

# This function intakes a filename and 2 index numbers
# It outputs a dictionary of dictionaries, where outer_index is the source for outer keys
# and the inner_index is the source of nested keys, organized by outer keys
# the inner dictionary contains keys / counts for each unique value in inner index
# The function also intakes a tuple (exp_val) of expected values which it uses to find user platforms


def twoD_dictplat(filename, outer_index, inner_index, exp_val):
    fh = open(filename)
    outerdict = {}
    for line in fh.readlines():
        eachline = line.split('\t')
        user_plat = find_shorten(exp_val,eachline[inner_index],"unclear")

        if eachline[outer_index] in outerdict:
            if user_plat in outerdict[eachline[outer_index]]:
                outerdict[eachline[outer_index]][user_plat] = outerdict[eachline[outer_index]][user_plat] + 1
            else:
                outerdict[eachline[outer_index]][user_plat] = 1
        else:
            outerdict[eachline[outer_index]] = {user_plat:1}
    return outerdict

# This function intakes a filename and 2 index numbers
# It outputs a dictionary of dictionaries, where outer_index is the source for outer keys
# and the inner_index is the source of nested keys, organized by outer keys
# the inner dictionary contains keys / counts for each unique value in inner index


def twoD_dict(filename, outer_index, inner_index):
    fh = open(filename)
    outerdict = {}
    for line in fh.readlines():
        eachline = line.split('\t')
        byvalue = eachline[inner_index]
        
        if eachline[outer_index] in outerdict:
            if byvalue in outerdict[eachline[outer_index]]:
                outerdict[eachline[outer_index]][byvalue] = outerdict[eachline[outer_index]][byvalue] + 1
            else:
                outerdict[eachline[outer_index]][byvalue] = 1
        else:
            outerdict[eachline[outer_index]] = {byvalue:1}
    return outerdict



# This function intakes a tuple of strings and a long string. If the any item in the tuple is found in the long string,
# then it will return that string value from the tuple. It is a case-insensitive search / return
# It also takes a third string which it returns in the case that nothing in the tuple is found.


def find_shorten(searchvals,longstring,alt_val):
    for el in searchvals:    
        if el.lower() in longstring.lower():
            return el
            break
    return alt_val

# This function intakes a dictionary of dictionaries and outputs a dictionary of the outer
# dictionary keys associated with the sum of the values of the inner dictionary within each
# outer dictionary key

def get_sumdict(mydict):
    outerkey_list = mydict.keys()

    countdict = {} #this is a new dictionary that stores the sum of the inner dict values

    for eachkey in outerkey_list:
        countdict[eachkey] = sum(mydict[eachkey].values())
    return countdict


# this function intakes a dictionary with all integer values and outputs a sorted list of the associated keys
def get_list(mydict):
    sorted_list = sorted(mydict,key = mydict.get)
    return sorted_list

# SCRIPT STARTS HERE
# -------------------------------

how_many, by_field, item = sys.argv[1:]

myfile = raw_input('Which file would you like me to look in? ')

fh = open(myfile)
headers = fh.readlines()[0].split('\t')
indexdict={}

how_manynum = int(how_many)

for column in headers:
    indexdict[column] = headers.index(column)

if by_field == 'platform':
    my_dictionary = twoD_dictplat(myfile,indexdict[item],1,platforms)
elif by_field not in indexdict:
    print ('Your second argument, what to sort, was incorrect. Try again. ')
    for key in indexdict:
        print key
    sys.exit()
elif item not in indexdict:
    print ('Your third argument, what to sort by, was incorrect. Try again. ')
    for key in indexdict:
        print key
    sys.exit()
else:
    my_dictionary = twoD_dict(myfile,indexdict[by_field],indexdict[item])

mycountdict = get_sumdict(my_dictionary)
mylist = get_list(mycountdict)

for i in range(0,how_manynum):
    print mylist[i]
    print my_dictionary[mylist[i]]
