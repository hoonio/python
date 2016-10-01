#!/usr/bin/env python
"""
Processing Images

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-04-17 (Mon, 17 Apr 2006) $"
__revision__ = "Homework 2"
#    Copyright (C) 2006 by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#
#	 Usage: ./montage.py (dirname) (number of pictures to montage)
#

import os, sys, re, string

if __name__ == '__main__':
	dirname, numpics = sys.argv[1], int(sys.argv[2])
	lspath = ["ls -R"] + [dirname] + ["> list"]
	os.system(string.join(lspath))
	list = open("list", 'r')
	ls = list.read()
	fnames = ls.split()
#	print fnames
	
	print dirname
#	os.chdir(dirname)
#	print os.system("pwd")

	montageset = []
	addpath = []
	addpath.append(dirname)
	addpath.append("/")
	print addpath

	picsatt = 0
	picindex = 0
	while picsatt < numpics:
		completepath = [fnames[picindex]]
		completepath = addpath + completepath
		temppath = string.join(completepath,'')
		completepath = ["identify"] + [temppath] + ["> id"]
		#completepath = string.join(addpath, fnames[i])
		#print completepath
		ident = 1									# for testing purpose
		ident = os.system(string.join(completepath))  # returns jpeg,png,gif
		#print "ident returns", ident
		iden = open("id", 'r')
		ide = iden.read()
		id = ide.split()
		if len(id):
			#print id
			if id[1] in ['JPEG','PNG','GIF']:
				montageset.append(temppath)
				picsatt += 1
				print "Collecting picture #", picsatt, "out of", numpics
		picindex += 1
	
	montageadd = ["montage"] + montageset + ["montage.png"]
	#print montageset
	#print montageadd
	montagecmd = string.join(montageadd)
	print "creating montage.png.......please wait"
	os.system(montagecmd)
	print "Done!!!"
