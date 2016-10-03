#!/usr/bin/env python
"""
Building a Remote iTunes Service

"""
__author__ = """Seunghoon Kim (ski819)"""
__date__ = "$Date: 2006-05-17 (Wed, 18 May 2006) $"
__revision__ = "Homework 4"
#    Copyright (C) 2006 by 
#    Seunghoon Kim <seunghoon@northwestern.edu>
#
#	 Executing python nettunes.py will trigger both functions.
#	 In order to modify arguments for the two functions, modify the last 3 lines of this code.
#	 Default values are host="wolverine", port=8080, seconds=20

import mytunes
import time

def average_track_length(remote_host, port):
	itunes = mytunes.MyTunes()
	itunes.start()
	try:
		tracks = itunes.track_length()
		count = len(tracks)
		total = sum(tracks)
		result = total/count
		return result
	except:
		print "Error retrieving tracks"

def needle_drop(remote_host, port, seconds):
	itunes = mytunes.MyTunes()
	try:
		tracks = itunes.track_length()
		count = len(tracks)
		itunes.play_track(0)
		for i in range(count):
			time.sleep(seconds)
			itunes.next_track()
			print "Playing next track"
	except:
		print "Error executing needle_drop"

print "Average track length:", average_track_length("wolverine", 8080)
print "Executing needle drop, will sample for 20 seconds"
needle_drop("wolverine", 8080, 20)