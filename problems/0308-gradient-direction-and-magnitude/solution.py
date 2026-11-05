import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here

	grad_array=np.array(gradient)
	magnitude=np.linalg.norm(grad_array)

	if magnitude==0.0:
		zero_vec=np.zeros_like(grad_array.tolist())
		return {
			"magnitude":0.0,
			"direction":zero_vec,
			"descent_direction":zero_vec



		}
	hat_d=a=np.divide(gradient,magnitude)
	d_final=np.multiply(hat_d,(-1))



	return {
		"magnitude":magnitude,
		"direction":hat_d.tolist(),
		"descent_direction":d_final.tolist()

	}


	pass