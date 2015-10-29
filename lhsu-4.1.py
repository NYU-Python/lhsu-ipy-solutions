#!/usr/bin/env python
import sys
import os
from time import time

class Logger:

    priorities = {critical:1,error:2,info:3,warning:4,debug:5}
    
    log_line_split = "    "

    def __init__(self,logfile, priority, datetime, scriptname):
        try:
            fh = open(logfile, 'r+')
            self.handle = fh
            self.name = logfile
            self.priority = priority
            self.datetime = datetime
            self.scriptname = scriptname
        except IOError, e:
            raise IOError("File can't be opened: {}".format(e))


    def lineitem(self,message):
        newline = []
        if self.datetime:
            newline.add(time.ctime())
        if self.scriptname:
            newline.add(os.path.basename(sys.argv[0]))
        stringline = ""
        for el in newline.add(message):
            stringline = stringline + Logger.log_line_split + el
        return stringline

    def critical(self,closefile, message):
        self.handle.write(lineitem(message))
        if closefile:
            self.handle.close()

    def error(self,closefile, message):
        self.critical(False,message)
        self.handle.write(lineitem(message))
        if closefile:
            self.handle.close()

    def warning(self,closefile, message):
        self.critical(False,message)
        self.error(False,message)
        self.handle.write(lineitem(message))
        if closefile:
            self.handle.close()

    def info(self,closefile, message):
        self.critical(False,message)
        self.error(False,message)
        self.warning(False,message)
        self.handle.write(lineitem(message))
        if closefile:
            self.handle.close()

    def debug(self,closefile, message):
        self.critical(False,message)
        self.error(False,message)
        self.warning(False,message)
        self.info(False,message)
        self.handle.write(lineitem(message))
        if closefile:
            self.handle.close()

