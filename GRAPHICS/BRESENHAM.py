from graphics import *

def bresenham(x1,y1,x2, y2):  
    m = 2 * (y2 - y1)  
    slope = m - (x2 - x1) 
  
    y=y1
    x=x1
    for x in range(x1,x2+1):
        win.plotPixel(x,y)
        print("(",x ,",",y ,")\n")  
        slope =slope + m  
        if (slope >= 0):  
            y=y+1
            slope =slope - 2 * (x2 - x1)





if __name__=="__main__":
    win=GraphWin("Bresenham",1000,1000)
    print("Enter the values of intial x and y coordinates: ")
    x1=int(input())
    y1=int(input())
    print("\n")
    print("Enter the values of final x and y coordinates: ")
    x2=int(input())
    y2=int(input())
    bresenham(x1,y1,x2,y2)
                
