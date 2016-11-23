# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 17:07:21 2016

@author: dmcme
"""
#This file just gives the number of current gpx activities
#the comma separations going. Then delete the first '0,'
#in the file before running this script.
#total 2016 485files

from numpy import loadtxt
lines = loadtxt("stravaurls.txt", comments="#", delimiter=",", unpack=False)

#the following gets the route numbers and inserts them into a URL for processing
with open('stravaurls.txt', 'r') as f:
    lines = f.read().split(",")
    print len(lines)