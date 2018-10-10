def insertlist(n,l,index=0):
    '''
     objective: To insert an element in the list.
     input:
       n:Any positive integer to be inserted in the list.
       l:List in which element is to be inserted.
       index: Internal parameter used as a counter variable.
     '''
    #Approach:Inserting the element recursively and using insert().
    if l==[]:
        l.insert(0,n)
    elif l[index:]==[]:
         l.append(n)
    elif l[index]>=n:
        l.insert(index,n)
    
    else:
          insertlist(n,l,index+1)

l=[1,4,6,9,14]
insertlist(3,l)
print(l)
