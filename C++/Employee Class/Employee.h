//guard
#ifndef EMPLOYEE_H
#define EMPLOYEE_H
#include <string>
using namespace std;
/**
header class file
*/

class Employee
{
public:
 void getData();
 void putData();
private:
 string name;
 long num;
};

#endif