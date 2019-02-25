from graphics import *
def drawcircle(x0, y0, r):
    x = r
    y = 0
    win.plotPixel(x0+x ,y0+y )
    if r>0:
        win.plotPixel(x0+x ,y0-y )
        win.plotPixel(x0+y ,y0+x )
        win.plotPixel(x0-y ,y0+x )

    p = 1-r
    while x>y:
        y=y+1
        if p<=0:
            p=p +2*y+1
        else:
            x=x-1
            p=p+2*y-2*x+1
        if x<y:
            break
        win.plotPixel(x0+x ,y0+y )
        win.plotPixel(x0-x ,y0+y )
        win.plotPixel(x0+x ,y0-y )
        win.plotPixel(x0-x, y0-y )

        if x!=y:
            win.plotPixel(x0+y ,y0+x )
            win.plotPixel(x0-y ,y0+x )
            win.plotPixel(x0+y ,y0-x )
            win.plotPixel(x0-y ,y0-x )

            

            


        
      
if __name__=="__main__":
    win=GraphWin("CIRCLE",10000,10000)
    print("Enter the values of intial x and y coordinates: ")
    x1=int(input())
    y1=int(input())
    print("\n")
    print("Enter the value of the radius: ")
    x2=int(input())
    drawcircle(x1,y1,x2)
                

    


            

        
