from random import randint 
import random
import numpy as np
import matplotlib.pyplot as plt

def chooserand(randomNumberList):
    temp = random.choice(randomNumberList)
    #temp = randomNumberList[0]
    randomNumberList.remove(temp)
    return temp

def reaction(finalb):
    
    k1=0.2
    k2=0.2
    T = 0
    deltaT=2
    numa = 4
    numb = 3
    N = numa + numb
    randomNumberList = [0.800, 0.801, 0.752, 0.661, 
                        0.169, 0.956, 0.949, 0.003, 
                        0.201, 0.291, 0.615, 0.131, 
                        0.241, 0.685, 0.116, 0.241, 0.849]
    i = 0
    while i < N :
        rand = chooserand(randomNumberList)
        if rand < numa/(numa+numb):
            rand = chooserand(randomNumberList)
            if rand < k1*deltaT:
                numa -= 1
                numb += 1
            else:
                pass
        else:
            rand = chooserand(randomNumberList)
            if rand < k2*deltaT:
                numa += 1
                numb -= 1
            else:
                pass
        #print("i = " + str(i),"numa = " + str(numa),"numb = " + str(numb))
        i += 1
        
    T += deltaT 
    finalb.append(numb)

if __name__ == "__main__":
    i = 0
    finalb = []
    runtimes = 100
    while i < runtimes:
        reaction(finalb)
        i +=1
    average_numb = np.mean(finalb)

    x = np.arange(1, runtimes+1, 1)
    fig, axs = plt.subplots(1,1)
    axs.plot(x, finalb,label="NumB")
    axs.axhline(y=average_numb, color='r', linestyle='-',label="averageNumB:"+str(average_numb))
    axs.set_xlim(0, runtimes+1)
    axs.set_xlabel('No. of recation')
    axs.set_ylabel('Value of B')
    axs.grid(True)
    fig.tight_layout()
    plt.legend(loc='upper left')
    plt.show()
    print(average_numb)