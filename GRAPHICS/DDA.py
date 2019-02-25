from graphics import *
def DDA(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    if abs(dx)>abs(dy):
        s = abs(dx)
    else:
        s = abs(dy)

    xinc = dx/s
    yinc = dy/s

    X = x1
    Y = y1
    for i in range(s):
        win.plotPixel(X,Y)
        print(abs(X),",",abs(Y))
        X+= xinc
        Y+= yinc
    win.plotPixel(X,Y)
    print(X,",",Y)



if __name__=="__main__":
    win=GraphWin("DDA Line",1000,1000)
    print("Enter the values of intial x and y coordinates: ")
    x1=int(input())
    y1=int(input())
    print("\n")
    print("Enter the values of final x and y coordinates: ")
    x2=int(input())
    y2=int(input())
    DDA(x1,y1,x2,y2)
    
    
        
