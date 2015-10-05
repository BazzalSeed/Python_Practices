#include <iostream>
#include <stdlib.h>
#include <math.h>  
// Peiyun Zeng
// HM5
//EXTra Credit DONE
using namespace std;
/* This Program  final value of the investment where the investment is fixed each year and compouned at fixed 
interest year every year.
This program requires user to input , either through interface or Commandline, three values, Respectively are
Investment amount, interest rate, number of years
*/

int main(int argc, char * argv[]){
	// Decalre the types of vriables
	int interest,money,years;
	double final;
    // ------------------------------------
	
	// Detect if user input info through command-line
	// if so take it, record it
	if (argc==4){
		money = atoi(argv[1]);
		interest = atoi(argv[2]);
		years = atoi(argv[3]);
	}
	// otherwise ask for needed info ( inverstment, interest rate, years) through interface
	else{
		cout<<"enter the initial investment amount(dollar): ";
		cin >> money;
		cout<<"enter the interest rate (percent): " ;
		cin >> interest;
		cout<< "enter the number of years: ";
		cin >> years;
		//cout<< "\n number of years: "<<years<<endl;
	}
	final = 0;
	// after get the needed info
	// caculate the final value of investment through a for loop
	for (int n = years; n > 0;n--){
		
		final = (money +final)*((interest/100.0)+1.0);
		
	}
	// output the final result
	cout<<"the final value of the investement is: ";
	cout<<final<<endl;
		


	return 1;
	
}