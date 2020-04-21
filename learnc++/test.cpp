#include <iostream>
#include <iomanip>
typedef double T;
using namespace std;
int main(){
	T tooktime = 2400;
  	int hour = tooktime/3600;
  	int minutes = (tooktime-hour*3600)/60;
  	int sec = tooktime-hour*3600 - minutes*60;  
	cout << "Simulation took : " <<  hour <<" hours, "<< minutes <<" minutes, "<< sec <<" seconds"<< std::endl;
}
