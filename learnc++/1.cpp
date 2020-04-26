#include <time.h>
#include <unistd.h>
#include <iostream>
#include <iomanip>
using namespace std;
typedef float T;

int it ;
int itconv=100;
int itmax=1000;
int itremain;
T timeperconv;
T timeremain;
T timetotal;
clock_t start, t2,endtime;

int main() {
    start=clock();
    it = 0;
    while (it < itmax){
        it = it + 1; 
        t2=clock();
        sleep(10000);
        if (it%itconv==0){
            t2 = clock() - t2;
            timeperconv = ((T) t2) / CLOCKS_PER_SEC;
            cout << "use = " << timeperconv << std::endl;
            itremain = itmax - it;
            timeremain = (itremain/itconv)*timeperconv;
            cout << "timeremain = " << timeremain << std::endl;
        }
    }
    endtime =  clock() - start;
    cout << "timeused = " << endtime / CLOCKS_PER_SEC << std::endl;
}

