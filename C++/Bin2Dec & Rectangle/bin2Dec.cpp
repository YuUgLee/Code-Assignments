/**
This function converts a binary string to a decimal number
@param binaryString string of binary representation
@return the decimal version of the given binary string
**/

#include <iostream>
#include <sstream>
using namespace std;

int bin2Dec(const string& binaryString)
{
 int length = binaryString.size();
 int decimalVal = 0;
 int base = 1; //2^0 = 1

 stringstream binary(binaryString);
 int temp = 0;
 binary >> temp;

 while(temp > 0)
 {
   int LSB = temp % 10; //to get the last digit
   temp /= 10; //continuously divide by 10 so the while loop will eventually end
   decimalVal += LSB * base; //add the sums
   base *= 2; //increment in power
 }

 return decimalVal;
}