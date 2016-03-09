#!/usr/bin/python
# -*- coding: utf-8 -*-

print '     _____           ____          ___        '
print '| /    |    |\   |  |    |    |\  |   | \   / '
print '|/     |    | \  |  |    |    | \ |___|  \ /  '
print '|\     |    |  \ |  |    |    | / |   |   |   '
print '| \  __|__  |   \|  |____|    |/  |   |   |   '

print'  ___ _____  ___  _____ _____  ___  _____ _____  __  ___'
print' |      |   |   |   |     |   |       |     |   |   |   ' 
print' |__    |   |___|   |     |   |__     |     |   |   |__ '    
print'    |   |   |   |   |     |      |    |     |   |      |'   
print' ___|   |   |   |   |   __|__ ___|    |   __|__ |__  __|'   


date=raw_input("Πληκτρολογείστε μια ημερομηνία  στην εξής μορφή(dd-MM-yyyy) και θα πάρετε τα ημερήσια στατιστικά του kino:")


import urllib2
req = urllib2.Request('http://applications.opap.gr/DrawsRestServices/kino/drawDate/' +str(date)+ '.json')
response = urllib2.urlopen(req)
the_page = response.read()

the_page=str(the_page)
the_page=the_page.split(",")
name=[]
p=2
l=22
for i in range (len(the_page)):
	if p<=3454:
		name+=[the_page[p:l:1]]
		p=p+22
		l=l+22		
name=str(name)

import re
int_list = [int(s) for s in re.findall('\\d+',name)]

for i in range (1,81):
	print i ,":" ,int_list.count(i)
