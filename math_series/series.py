def fibonacci(n):
    """  
      This function executes the fibonacci sequence based on the parameter n. n is evaluated against the base cases of the fibonacci sequence, if neither base case is true, the fibonacci sequence is run based on n.

    """    
    if n==0:
        return 0
    if n==1:
        return 1    
    return  fibonacci(n-1)+fibonacci(n-2)

def lucas(n):    
    """  This function executes the lucas sequence based on the parameter n. n is evaluated against the base cases of the lucas sequence, if neither base case is true, the lucas sequence is run based on n. 

    """
    if n==0:
        return 2
    if n==1:
        return 1
    return  lucas(n-1)+lucas(n-2)
    



def sum_series(n,para2=0,para3=1):
    """ 
      This function executes a fibonnaci/lucas style formula on the given parameters. The first parameter is the n that you wish the formula to execute on. The second is an optional base case of nth = 0. The third is an optional base case of nth = 1. If the last two arguments are ecluded, this function will execute as a fibbonaci sequence based on n. 

    """
    if  n==0:
        return para2
    if n==1:
        return para3   
    return  sum_series(n-1,para2,para3)+sum_series(n-2,para2,para3)

