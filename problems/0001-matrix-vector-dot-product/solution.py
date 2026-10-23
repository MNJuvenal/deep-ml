def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	an,am=len(a),len(a[0])
	bn=len(b)
	X=[0 for i in range(an) ]
	if am!=bn:

		return -1 


	for i in range(an):			
			for k in range(bn):
				X[i]+=(a[i][k]*b[k])
	return X

	pass