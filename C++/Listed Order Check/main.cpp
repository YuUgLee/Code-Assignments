#include <iostream>
using namespace std;
/*
Program creates a list based on user input and checks if it's in a listed order
@author Newton Bao
@author
Version Fall 2020
Date:September 21,2020
*/

//Method checks if list is in sorted order
//@param array of the list and size of the list 
//@return true or false
bool isSorted(const int list[], int size){
  for (int i=0;i<size-1;i++){
    if (list[i]>list[i+1]){
      return false;
    }
  }
  return true;
}
int main() {
  int arr[100];
  int size;
  cin>>size;
  cout<<"Enter input:"<<endl;
  for (int i=0;i<size;i++){
    cin>>arr[i];
  }
  if (isSorted(arr,size)==true){
    cout<<"List is sorted"<<endl;
  }
  else{
    cout<<"List is not sorted"<<endl;
  }

} P1