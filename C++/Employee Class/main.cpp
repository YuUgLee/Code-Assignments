#include <iostream>
#include "Employee.h"
#include <string>
using namespace std;
/*
Program collects Name and Employee Number from user input and prints it 
@author Newton Bao
@author
Version Fall 2020
Date:September 21,2020
*/
int main() {
  //Declares Employee object array
  Employee arr[3];
  int i=0;
  cout<<"Enter Employee Data "<<endl;
  //retrieves data while less than size of array
  while (i!=3){
    arr[i].getData();
    i++;
  }
  i=0;
  cout<<"Employee Data"<<endl;
  //prints data while less than size of array
  while (i!=3){
    arr[i].putData();
    cout<<endl;
    i++;
  }
}