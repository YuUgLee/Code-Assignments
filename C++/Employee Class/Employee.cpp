#include "Employee.h"
#include <iostream>
#include <string>
using namespace std;
//Collects data from user input
void Employee :: getData(){
cout<<"Enter name: ";
cin>>name;
cout<<"Enter number: ";
cin>>num;
}
//Prints data from user input
void Employee :: putData(){
  cout<<"Name: "<<name<<endl;
  cout<<"Number: "<<num<<endl;
}