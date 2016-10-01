#!/usr/bin/env python
"""
Regular Expression II

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-04-17 (Mon, 17 Apr 2006) $"
__revision__ = "Homework 2"
#    Copyright (C) 2006 by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#


import re, fileinput

pattern = re.compile(r'''(?x)( # verbose identify URLs within text
	(http|ftp|gopher|mailto|telnet|file|wais) # make sure we find a resource type
	:* # ...needs to be followed by colon-slash-slash
	[^ \n\r]+ # some stuff then space, newline, tab is URL
	(\w+\.?){2,} # at least two domain groups, e.g. (gnosis.)(cx)
	(?=[\s\.,]) # assert: followed by whitespace/period/comma
	) # end of match group
	''')

#for line in fileinput.input():
if __name__ == '__main__':
	for line in fileinput.input():
		print re.compile(pattern, re.M).sub("<a href=\"\g<0>\">\g<0></a>", line.rstrip())
