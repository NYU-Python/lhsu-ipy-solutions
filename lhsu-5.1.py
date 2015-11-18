#!/usr/bin/env python

class PersistDict(dict):
    
    def __init__(self,filename):
        self.dictionary = dict.__init__(self)
        self.filename = filename + ".csv"
        try:
            self.copy_file()
        except:
            self.dictionary = {}           
        
    def __setitem__(self, key, value):
        dict.__setitem__(self.dictionary, key, value)
        print 'setitem'
        print self.dictionary
        self.write_file()
    
    def __delitem__(self,key):
        dict.__delitem__(self.dictionary,key)
        self.write_file()
    
    #This method clears the dictionary stored in the instance, as well as the file
    def clear(self):
        dict.clear(self.dictionary)
        self.write_file()

        
    #This method updates the dictionary stored in the instance (self) that with the
    #values in newdict (passed argument)
    def update(self,newdict):
        if type(newdict) is dict:
            dict.update(self.dictionary,newdict)
        else:
            dict.update(self.dictionary,newdict.dictionary)
        self.write_file()
    
    #This method writes the dictionary into the filename stored in the object
    #as a CSV
    def write_file(self):
        fh = open(self.filename,"w")
        mydict = self.dictionary
        mylines = []
        print 'writefile'
        print mydict
        for item in mydict.keys():
            eachline = item+","+mydict[item]+'\n'
            print eachline
            mylines.append(eachline)
            
        fh.writelines(mylines)
        
        fh.close()
        
    #This method allows the user to copy a dictionary from a CSV file into the 
    #instance's dictionary
    def copy_file(self):
        fh = open(self.filename)
        mydict = {}
        for line in fh.readlines():
            columns = line.split(",")
            mydict[columns[0]] = columns[1]
        self.dictionary = mydict
