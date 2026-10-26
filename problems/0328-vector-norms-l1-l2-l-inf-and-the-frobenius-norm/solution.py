import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
     
    res=0
    if arr.ndim==2:
        arr_l,arr_c=arr.shape

    if norm_type=='l1':
         
        if arr.ndim==1:
            for i in range(len(arr)):
                res+=abs(arr[i])
            return float(res) 
        else:
            
            for i in range(arr_l):
                for j in range(arr_c):
                    res+=abs(arr[i][j])
            return float(res)

    elif norm_type=='l2':

        if arr.ndim==1:
            for i in range(len(arr)):
                res+=arr[i]**2
            return float(np.sqrt(res))
        else :
            for i in range(arr_l):
                for j in range(arr_c):
                    res+=(arr[i][j])**2
            return float(np.sqrt(res))

    elif norm_type=='linf':
        #even if is 1D or 2D vectors it's always return the max of  all values encoutered   
        return float(np.max(np.abs(arr)))
    
    elif norm_type=='frobenius' and arr.ndim==2:

        for i in range(arr_l):
            for j in range(arr_c):
                res+=(arr[i][j])**2
        return float(np.sqrt(res))

    else :
        raise ValueError(f"Norme non reconnue : {norm_type}") 

    pass
