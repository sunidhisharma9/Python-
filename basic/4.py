def sumList(a):
    '''
    Objective: To compute the sum of list of integers.
    Input parameters:
        a: list of integers whose sum we have to calculate.
    Output:
        Sum of list of integers.
    '''
    #Approach: Recurrsion- sumList(a) = a[0] + sumList(a[1:])

    if a==[]:
        return 0
    else:
        return a[0] + sumList(a[1:])
