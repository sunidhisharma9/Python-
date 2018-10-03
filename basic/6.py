def succ(N):
    '''
    OBJECTIVE: To find the successor of a number.
    INPUT PARAMETER:
          N: a non-negative number whose successor is to be calculated.
    OUTPUT:
          Successor of non-negative number 'N'.
    '''
    #Approach: succ(N) = N+1

    if N>=0:
        return N+1
    print("Error: ",N," < 0.")
    return


#assert N>=0


def pred(N,i=0):
    '''
    OBJECTIVE: To find predecessor of a number.
    INPUT PARAMETER:
          N: a positive number whose predecessor is to be calculated.
          i: candidate for finding predecessor (default parameter)
    OUTPUT:
           Predecessor of non-negative number 'N'.
    '''
    #Approach: if succ(X)==N, then pred(N)==X ,where 0 <= X < N
    
    assert N>0
    if succ(i)==N:
        return i
    else:
        return pred(N,i+1)
        
