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


def mergelist(l1,l2,index=0):
    '''
     objective:To insert elements of unsorted list l2 in sorted list l1 such that l1 remians sorted.
       input:
         l1: A sorted list.
         l2: An unsorted list.
         index:Internal parameter.
     '''
    #Approach:Inserting elements recursively using insertlist() function.
    if l2[index:]==[]:
      return
    else:
        insertlist(l2[index],l1)
        mergelist(l1,l2,index+1)

l1=[1,3,7,9]
l2=[0,8,4,6]
mergelist(l1,l2)
print(l1)
    
