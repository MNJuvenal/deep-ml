def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.

	a_l=len(a)
	b_l=len(b)
	
	if a_l!=b_l:
		return -1
	return [i+j  for i,j in zip(a,b) ]

	

	pass