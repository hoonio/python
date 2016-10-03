#!/usr/bin/env python
"""
Extension Setup File

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-04-17 (Mon, 17 Apr 2006) $"
__revision__ = "Homework 3"
#    A Script written by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#

from distutils.core import setup, Extension

module = Extension('rankorder', sources = ['rankorder.c'])

setup (name = 'rank_order',
	   version = '1.0',
	   description = 'CS495-20 MP3',
	   ext_modules = [module])