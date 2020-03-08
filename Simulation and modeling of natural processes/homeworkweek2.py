
import numpy as np
import math
import matplotlib.pyplot as plt

class Integrator:
    def __init__(self, xMin, xMax, N):
        ################################
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
            
    def integrate(self):

        deltaX = (self.xMax-self.xMin)/self.N
        self.ans = []
        self.xvalue = []
        self.fvalue = []
        self.sum = 0
        for i in range (0,self.N):
            xi = self.xMin + i * deltaX
            f = function(xi)
            ans = f * deltaX
            self.fvalue.append(f)
            self.sum += ans
            self.xvalue.append(xi)
            self.ans.append(self.sum)
        
    def show(self):

        print(self.sum)
        fig, axs = plt.subplots(1,1)
        axs.plot(self.xvalue, self.ans,label="Ans")
        axs.plot(self.xvalue, self.fvalue,label="function")
        axs.set_xlim(0, self.xMax+1)
        axs.set_xlabel('X')
        axs.set_ylabel('Value')
        axs.grid(True)
        fig.tight_layout()
        plt.legend(loc='upper left')
        plt.show()

def function(x):
    return math.exp(-x)*math.sin(x)*x**2
        
if __name__ == "__main__":

    examp = Integrator(1,3,200000)
    examp.integrate()
    examp.show()