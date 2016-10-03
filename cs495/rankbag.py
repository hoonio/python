#	Return a dictionary where
#	key = rank, ranked by number of occurrences
#	val = number of numbers at that rank
#	There may be more elegant ways to do this but
#	this is the most straightforward I could come up with.

import types

class RankBag(list):
	def __init__(self, list):
		self = list
		print self
	
	def rank(self):
		# Calculate the number of occurrences of a given number
		occurrences = {}
		for i in range(len(self)):
			occurrences[(self[i])] = occurrences.setdefault((self[i]), 0 ) + 1
		# Construct a decreasingly sorted sequence of
		# cnt, num pairs, first pair has rank 1
		self = [(cnt, num) for num, cnt in occurrences.items()]
		print self
		self.sort()
		print self
		self.reverse()
		print self
		return self
	
#	rank_counts = {}
#	current_rank = 1
#	current_cnt = pairs[0][0]
#	print current_cnt
	
	# Build the final dictionary, looking for transitions in
	# the counts for a number
#	for cnt, num in pairs:
#		print cnt, current_cnt
#		if cnt <> current_cnt:
#			current_rank = current_rank + 1
#			current_cnt = cnt
#		rank_counts[current_rank] = rank_counts.setdefault(current_rank, 0) + 1
		
#	print rank_counts
#	return rank_counts