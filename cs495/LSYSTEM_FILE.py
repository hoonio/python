#!/usr/bin/env python
"""
L-systems file for RGS

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-06-11 (Sun, 11 Jun 2006) $"
__revision__ = "Homework 5"
#    A Script written by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#

import sys,re

start = "F"
iterations = 3
rules = {"F": "F+F--F+F"}
	
def generate():	
	pattern = start
	for i in range(iterations):
		pattern = re.sub(start, rules[start], pattern)	
#		print pattern
	return pattern	
