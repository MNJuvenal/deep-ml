def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    #based on the formul the derivate of c*x^n is c*n*x^(n-1)

    return c*n*(x**(n-1))
    pass