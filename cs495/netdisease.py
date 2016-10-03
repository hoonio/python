#!/usr/bin/env python
"""
Simulating Spread of Disease in Networks

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-04-10 (Mon, 10 Apr 2006) $"
__revision__ = "Homework 1"
#    Copyright (C) 2006 by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#
#	 Note: Higher numbered nodes are more likely to die after their first cycle as infected,
#			while more likely to recover from infected state.

from networkx import *
import random

def netdisease(n,k,s,p,i):
	
	Infected=[]
	Dead=[]
	G=Graph()
	d=0.2			# sustain rate for infected
	r=0.05			# recovery rate for infected, the remainder survives without recovery
	for m in range(n):
		G.add_node(int(m))
		if ((m%100) == 0):
			Infected.append(int(m))
		for l in range(k):
			t=m+int(l*n*s/k)				# rewire proability calculated
			if t>n:
				t = t-n
			G.add_edge( (int(m),int(t)) )
	for j in range(i):
		for c in range(len(Infected)):
			if c < r*len(Infected):
				Infected.pop()
		Dead.extend(Infected)
		for c in range(len(Infected)):
			Infected.pop()
		for a in range(n):
			if a in Dead:
				B=G.degree(a)
				for b in range(B):
					newinfect = G[a][b]
					if b < p*B:
						if newinfect not in Infected:
							if newinfect not in Dead:
								Infected.append(int(newinfect))
		for c in range(len(Dead)):
			if c > d*len(Dead):				# clear dead list according to the death rate
				G.delete_node(Dead[len(Dead)-1])
				Dead.pop()

	S= G.number_of_nodes() * 100 / n
	print '--------------------------------------------------'
	print 'Disease spread Simulation by Seunghoon Kim(ski819)'
	print 'Percentage of Survivors = ', S,'%'
	print 'Recovery and sustain rate can be configured by' 
	print 'manually changing the value in netdisease.py'
	print '--------------------------------------------------'
	
	return G.number_of_nodes()