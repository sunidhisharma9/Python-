def swap(l,li=0,i=9):
    '''
     objective: To place the largest number in the list at the first position.
     input:
       l: List of positive integers.
       li:Lower index.(internal parameter)
       i:Upper index.(internal parameter)
     '''
    #Approach: Recursively swapping numbers to get the largest integer of the list at the first position.
    
    if l==[]:
        return
    elif i==li:
        return
    
    elif l[i]>=l[i-1]:
        temp=l[i]
        l[i]=l[i-1]
        l[i-1]=temp
    swap(l,li,i-1)

       
def bubble(l,li=0,i=9):
    if l==[]:
        return
    elif li==9:
        return
    else:
        swap(l,li,i)
        bubble(l,li+1,i)

    
