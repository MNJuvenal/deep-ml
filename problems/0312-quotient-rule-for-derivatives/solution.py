import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    #accordind to the formula the derivate fonction of f=g/h equal f'=g'*h-g*h'/h^2 wiyht h!=0
    exp_max_g=len(g_coeffs)-1
    exp_max_h=len(h_coeffs)-1


    if x==float((0)):
        return float((-1))
    #let's compute g'
    
    g_prime=sum([((exp_max_g-i)*j)*(x**((exp_max_g-i)-1)) for i,j in enumerate(g_coeffs)])

    #h' prime the same idea that g'
    h_prime=sum([((exp_max_h-i)*j)*(x**((exp_max_h-i)-1)) for i,j in enumerate(h_coeffs)])

    h=sum([j*(x**((exp_max_h-i))) for i,j in enumerate(h_coeffs)])
    
    g=sum([j*(x**((exp_max_g-i))) for i,j in enumerate(g_coeffs)])
    
    return ((g_prime*h)-(g*h_prime))/(h**2)
    # Your code here
    pass