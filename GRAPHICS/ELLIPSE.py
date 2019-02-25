from graphics import *
def drawellipse(xc,yc,rx,ry):
        #region1
        p=ry*ry-rx*rx*ry+rx*rx/4
        x=0
        y=ry
        while 2*ry*ry*x <= 2*rx*rx*y:
            if p < 0:
                x=x+1
                p = p+2*ry*ry*x+ry*ry
            else:
                x=x+1
                y=y-1
                p = p+2*ry*ry*x-2*rx*rx*y-ry*ry
            win.plotPixel(xc+x,yc+y)
            win.plotPixel(xc+x,yc-y)
            win.plotPixel(xc-x,yc+y)
            win.plotPixel(xc-x,yc-y)
        #region2
        p=ry*ry*(x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
        while(y > 0):
            if(p <= 0):
                x=x+1
                y=y-1
                p = p+2*ry*ry*x-2*rx*rx*y+rx*rx
            
            else:
                y=y-1
                p = p-2*rx*rx*y+rx*rx
        
            win.plotPixel(xc+x,yc+y)
            win.plotPixel(xc+x,yc-y)
            win.plotPixel(xc-x,yc+y)
            win.plotPixel(xc-x,yc-y)
       
if __name__=="__main__":
        win=GraphWin("ELLIPSE",1000,1000)
        print("Enter the values of intial x and y coordinates of the centre: ")
        x1=int(input())
        y1=int(input())
        print("\n")
        print("Enter the values of final x and y coordinates of the radius: ")
        x2=int(input())
        y2=int(input())
        drawellipse(x1,y1,x2,y2)
                    
