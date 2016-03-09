#!/usr/bin/python
# -*- coding: utf-8 -*-
print '\t     ____ _____              '
print '\t    |       |    |\   |  |\     '
print '\t    |___    |    | \  |  | \    '
print '\t    |       |    |  \ |  | /       '
print '\t    |     __|__  |   \|  |/  '

print '   _____       ____          ___        '
print '     |   |  | |         |\  |   | \   / '
print '     |   |__| |___      | \ |___|  \ /  '
print '     |   |  | |         | / |   |   |   '
print '     |   |  | |____     |/  |   |   |   '

import math
r=raw_input("Enter a date(XX/XX/XXXX): ").split('/')
arith=int(r[0])
mhn=int(r[1])
xron=int(r[2])
#orizw mia mera 1/01/2016 kai to day deixnei thn mera (5=paraskevi)
arithmos=1
mhnas=1
xronia=2016
day=5
#ypologizv thn diafora metaxi ths statherhs kai auths tou xristi se apoliti timi
diaf=math.fabs(xronia-xron)
#metraw ta disekta
cdisekta=0
k=int(xron+diaf)
if (arith==arithmos and mhn==mhnas and xron==xronia):
		print "ΠΑΡΑΣΚΕΥΗ"		
else:
	tsoubali1=0
	tsoubali=0
	if xron<xronia:
		for i in range (xron+1,k):
			if (i%4==0) and (i%100!=100):
				cdisekta+=1
		tsoubali1=cdisekta*366+(diaf-cdisekta)*365
		if (xron%4==0) and (xron%100!=100):
			if mhn==1:
				tsoubali=335+(31-arith)
			if mhn==2:
				tsoubali=306+(29-arith)
			if mhn==3:
				tsoubali=275+(31-arith)
			if mhn==4:
				tsoubali=245+(30-arith)
			if mhn==5:
				tsoubali=214+(31-arith)
			if mhn==6:
				tsoubali=184+(30-arith)
			if mhn==7:
				tsoubali=153+(31-arith)
			if mhn==8:
				tsoubali=122+(31-arith)
			if mhn==9:
				tsoubali=92+(30-arith)
			if mhn==10:
				tsoubali=61+(31-arith)
			if mhn==11:
				tsoubali=31+(30-arith)
			if mhn==12:
				tsoubali=31-arith
		else:
			if mhn==1:
				tsoubali=334+(31-arith)
			if mhn==2:
				tsoubali=306+(28-arith)
			if mhn==3:
				tsoubali=275+(31-arith)
			if mhn==4:
				tsoubali=245+(30-arith)
			if mhn==5:
				tsoubali=214+(31-arith)
			if mhn==6:
				tsoubali=184+(30-arith)
			if mhn==7:
				tsoubali=153+(31-arith)
			if mhn==8:
				tsoubali=122+(31-arith)
			if mhn==9:
				tsoubali=92+(30-arith)
			if mhn==10:
				tsoubali=61+(31-arith)
			if mhn==11:
				tsoubali=31+(30-arith)
			if mhn==12:
				tsoubali=31-arith
		teliko=tsoubali1+tsoubali+1
		if teliko%7==2:
			print 'ΠΕΜΠΤΗ'
		if teliko%7==3:
			print 'ΤΕΤΑΡΤΗ'
		if teliko%7==1:
			print 'ΠΑΡΑΣΚΕΥΗ'
		if teliko%7==5:
			print 'ΔΕΥΤΕΡΑ'
		if teliko%7==6:
			print 'ΚΥΡΙΑΚΗ'
		if teliko%7==0:
			print 'ΣΑΒΒΑΤΟ'
		if teliko%7==4:
			print 'ΤΡΙΤΗ'
	elif xron==xronia:
		if mhn==1:
			tsoubali=arith
		if mhn==2:
			tsoubali=31+arith
		if mhn==3:
			tsoubali=60+arith
		if mhn==4:
			tsoubali=91+arith
		if mhn==5:
			tsoubali=121+arith
		if mhn==6:
			tsoubali=152+arith
		if mhn==7:
			tsoubali=182+arith
		if mhn==8:
			tsoubali=213+arith
		if mhn==9:
			tsoubali=244+arith
		if mhn==10:
			tsoubali=274+arith
		if mhn==11:
			tsoubali=305+arith
		if mhn==12:
			tsoubali=335+arith
		if tsoubali%7==0:
			print 'ΠΕΜΠΤΗ'
		if tsoubali%7==6:
			print 'ΤΕΤΑΡΤΗ'
		if tsoubali%7==1:
			print 'ΠΑΡΑΣΚΕΥΗ'
		if tsoubali%7==4:
			print 'ΔΕΥΤΕΡΑ'
		if tsoubali%7==3:
			print 'ΚΥΡΙΑΚΗ'
		if tsoubali%7==2:
			print 'ΣΑΒΒΑΤΟ'
		if tsoubali%7==5:
			print 'ΤΡΙΤΗ'
	else:
		for i in range (xron-1,xronia,-1):
			if (i%4==0) and (i%100!=100):
				cdisekta+=1	
		tsoubali1=(cdisekta+1)*366+(diaf-(cdisekta+1))*365
		if (xron%4==0) and (xron%100!=100):
			if mhn==1:
				tsoubali=arith
			if mhn==2:
				tsoubali=31+arith
			if mhn==3:
				tsoubali=60+arith
			if mhn==4:
				tsoubali=91+arith
			if mhn==5:
				tsoubali=121+arith
			if mhn==6:
				tsoubali=152+arith
			if mhn==7:
				tsoubali=182+arith
			if mhn==8:
				tsoubali=213+arith
			if mhn==9:
				tsoubali=244+arith
			if mhn==10:
				tsoubali=274+arith
			if mhn==11:
				tsoubali=305+arith
			if mhn==12:
				tsoubali=335+arith
		else:		
			if mhn==1:
				tsoubali=arith
			if mhn==2:
				tsoubali=31+arith
			if mhn==3:
				tsoubali=59+arith
			if mhn==4:
				tsoubali=90+arith
			if mhn==5:
				tsoubali=120+arith
			if mhn==6:
				tsoubali=151+arith
			if mhn==7:
				tsoubali=181+arith
			if mhn==8:
				tsoubali=212+arith
			if mhn==9:
				tsoubali=243+arith
			if mhn==10:
				tsoubali=273+arith
			if mhn==11:
				tsoubali=304+arith
			if mhn==12:
				tsoubali=334+arith			
		teliko=tsoubali+tsoubali1
		if teliko%7==0:
			print 'ΠΕΜΠΤΗ'
		if teliko%7==6:
			print 'ΤΕΤΑΡΤΗ'
		if teliko%7==1:
			print 'ΠΑΡΑΣΚΕΥΗ'
		if teliko%7==4:
			print 'ΔΕΥΤΕΡΑ'
		if teliko%7==3:
			print 'ΚΥΡΙΑΚΗ'
		if teliko%7==2:
			print 'ΣΑΒΒΑΤΟ'
		if teliko%7==5:
			print 'ΤΡΙΤΗ'
