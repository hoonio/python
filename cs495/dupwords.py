#!/usr/bin/env python
"""
Regular Expression I

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-04-17 (Mon, 17 Apr 2006) $"
__revision__ = "Homework 2"
#    Copyright (C) 2006 by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#

import sys
import re
import glob

for pat in sys.argv[1:]:
	for file in glob.glob(pat):
		for para in open(file).read().split('\n\n'):
			dups = re.findall(r'(?m)(^.*(\b\w+\b)\s*\b\2\b.*$)', para)
			if dups:
				for dup in dups:
					print 'Duplicate word "%s" found in sequence: ' % dup[1], dup[0]						  

