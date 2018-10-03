def sumUpTo(n):
    '''
    Objective: To compute the sum of first 'n' whole numbers.
    Input:
        n: A whole number 'n' upto which we have to calculate the sum.
    Output:
        Sum of first 'n' whole numbers.
    '''
    #Approach: Recurrsion- sumUpTo(n) = n + sumUpTo(n-1)

    if n==0:
        return 0
    else:
        return n+ sumUpTo(n-1)
