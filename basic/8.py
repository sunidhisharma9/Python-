def areaRectangle(l,b=1):
    '''
     OBJECTIVE: to calculate the area of a rectangle.
     INPUT PARAMETERS:
           l: length of rectangle (non-negative)
           b: breadth of rectangle (non-negative)
     OUTPUT:
           printing the area of given rectangle.
    '''
    #Approach: area = length * breadth

    assert l>=0
    assert b>=0
    area=l*b
    print("Area = ",area)
           
