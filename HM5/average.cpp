#include <iostream>
#include <stdlib.h>
#include <sstream>
// Peiyun Zeng
// Homeowrk 5
using namespace std;

int main(){
	/* This program caculates the average of user inputs
	it will ask you to input the value and the first negative input will terminate the program
	the average exclude the terminator(the negative value)
	*/
	
	
	// ------------------------------------------
	//Declare the types of variables
	double sum = 0 ;
	double read=1;
	double average;
	int count = 0;
	// ——————————————————————————————————————————
	
    // While loop will ask the input from the suer
	// Add this input to the sum
	while(read > 0){
		cout << "Please ENter the number: ";
		cin >>read;
		count++;
		// print out what read in
		cout<<"read is: ";
		cout<<read<<endl;
		if(read>0){
			sum += read;	
		}
        // print out the current sum
		cout<<"the sum: ";
		cout<<sum<<endl;
	}
	count -=1;
	// print out how many numbers entered( excludes the last negative number)
	cout<<"the count is: ";
	cout<<count<<endl;
	//Caculate the Average
	average = sum/count;
    // Print out the average
	cout<<"\nThe average of the sequence is : "<< average<<endl; 
	
	
}