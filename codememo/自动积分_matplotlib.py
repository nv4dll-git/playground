
import numpy as np
import math
import matplotlib.pyplot as plt

class plot:

    def __init__(self):
        self.fig, self.axs = plt.subplots(1,1)
        self.axs.set_xlabel('X')
        self.axs.set_ylabel('Value')
        self.axs.grid(True)
        self.fig.tight_layout()
        
    def addplot(self,x,y,color,label):
            self.axs.plot(x, y, color, label=label)
            plt.legend(loc='upper left')

    def show(self):
            plt.show()

class Integrator:
    def __init__(self, xMin, xMax, N):
        ################################
        self.xMin = xMin
        self.xMax = xMax
        self.N = N

    def getIntegrationTime(self,deltaX):
        return np.arange(self.xMin,self.xMax,deltaX)

    def integrate(self):
        deltaX = (self.xMax-self.xMin)/self.N
        self.ans = np.zeros(self.N)
        self.xvalue = self.getIntegrationTime(deltaX)
        self.fvalue = np.zeros(self.N)
        self.sum = 0
        for i in range (0,self.N):
            xi = self.xMin + i * deltaX
            f = function(xi)
            ans = f * deltaX
            self.fvalue[i]=f
            self.sum += ans
            self.xvalue[i] = xi
            self.ans[i] = self.sum
        
    def show(self):

        print(self.sum)
        plot1 = plot()
        plot1.addplot(self.xvalue,self.fvalue,'r-',"Ans")
        plot1.addplot(self.xvalue,self.ans,'b-',"function")
        plot1.show()
        
def function(x):
    return math.exp(-x)*math.sin(x)*x**2
        
if __name__ == "__main__":

    examp = Integrator(1,3,200000)
    examp.integrate()
    examp.show()