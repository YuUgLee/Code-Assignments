/**
This program converts binary numbers into decimal values, as well as creating Rectangle objects and displaying their dimensions, areas, and perimeters
@author Sydney Kao and Newton Bao
@version Fall 2020
@date 8/26/2020
*/

#include <iostream>
#include "Rectangle.h"
using namespace std;

//prototype, defined in bin2Dec.cpp
int bin2Dec(const string& binaryString);

/**
The tester that runs the program
*/
int main()
{
  string binary;
  cout << "Enter a binary number: ";
  cin >> binary;
  cout << "Decimal value: " << bin2Dec(binary) << endl;

  Rectangle r1;
  r1.setWidth(4);
  r1.setHeight(40);

  Rectangle r2;
  r2.setWidth(3.5);
  r2.setHeight(35.9);

  cout << "\nRectangle 1:\n";
  cout << "Width: " << r1.getWidth() << " Height: " << r1.getHeight() << endl;
  cout << "Area: " << r1.getArea(r1.getWidth(), r1.getHeight()) << " Perimeter: " << r1.getPerimeter(r1.getWidth(), r1.getHeight()) << endl;

  cout << "\nRectangle 2:\n";
  cout << "Width: " << r2.getWidth() << " Height: " << r2.getHeight() << endl;
  cout << "Area: " << r2.getArea(r2.getWidth(), r2.getHeight()) << " Perimeter: " << r2.getPerimeter(r2.getWidth(), r2.getHeight()) << endl;
  
  return 0;
}