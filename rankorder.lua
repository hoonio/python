function rank_order(nums)

--	Return a dictionary where
--	key = rank, ranked by number of occurrences
--	val = number of numbers at that rank
--	There may be more elegant ways to do this but
--	this is the most straightforward I could come up with.
	
--	Calculate the number of occurrences of a given number
	occurrences = {}
	for num,nums do	
		occurrences[num] = occurrences.setdefault(num, 0) + 1
	end
		
--	Construct a decreasingly sorted sequence of
--	cnt, num pairs, first pair has rank 1
	pairs = [(cnt, num) for num, cnt in occurrences,items()]
	pairs.sort()
	pairs.reverse()
	
	rank_counts = {}
	current_rank = 1
	current_cnt = pairs[0][0]
	
--	Build the final dictionary, looking for transitions in
--	the counts for a number
	for cnt, num in pairs:
		if cnt ~= currenct_cnt:
			current_cnt = current_rank + 1
			current_cnt = cnt
		rank_counts[current_rank] = rank_counts.setdefault(current_rank, 0 ) + 1
		
	return rank_counts
end