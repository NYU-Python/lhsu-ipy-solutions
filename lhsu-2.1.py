#!/usr/bin/env python


import sys
import os

# FUNCTIONS
# ------------------
# function to take a list of strings and output a dictionary
# the key is separated from its value with an "="
def make_dict(listostrings):
    output_dict = {}
    for item in listostrings:
        separated_item = item.split('=')
        output_dict[separated_item[0]] = separated_item[1]
    return output_dict

# function intakes three sets and verifies whether they are required values are present, and all values are valid
# outputting a boolean
# It also prints error text when the validation rejects the inputs
def compare_sets(master_set,required_set,test_set):
    if test_set.issuperset(required_set):
        if test_set.issubset(master_set):
            return True
        else:
            print ('You have included an invalid field. Acceptable fields include:')
            print (master_set)
            return False
    else:
        print ('You are missing one of the required fields:')
        print (required_set)
        return False

# This function takes in a dictionary containing 2-4 email fields and outputs a 
# formatted, triple-quoted string containing the info
def header_printer(email_dictionary):
    each_line = '''{}: {}\n'''
    req_fields = each_line.format('from',email_dictionary['from'])+each_line.format('to',email_dictionary['to'])
    if 'subject' in email_dictionary:
        updated_string = req_fields + each_line.format('subject',email_dictionary['subject'])
    else:
        updated_string = req_fields + each_line.format('subject','[no subject]')
    if 'body' in email_dictionary:
        output_string = updated_string + each_line.format('body',email_dictionary['body'])
    else:
        output_string = updated_string + each_line.format('body','')
    
    return output_string

# SCRIPT
# --------------------------

sendmail_prog = '/usr/sbin/sendmail'   # mac default.  use
                                       # 'which sendmail' to locate
                                       # sendmail on unix/linux

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])

args = sys.argv[1:]


mydictionary = make_dict(args)

validcheck = compare_sets(valid_args,required_args,set(mydictionary.keys()))

if validcheck == False:
    print ('Try again. I could not understand your arguments.')
else:
    my_output = header_printer(mydictionary)
    print my_output


