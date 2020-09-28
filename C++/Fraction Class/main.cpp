/*
This program creates Fractions and tests its behaviors including printing, setting 
numberators and denominators, and multiplying fractions.
@author Sydney Kao and Newton Bao 
@version Fall 2020
@date September 14, 2020
*/

#include "Fraction.h"
#include <iostream>
using namespace std;

Fraction& multiplyFract (Fraction& fr1, Fraction& fr2);

int main ( )
{
    // Instantiation of some objects
    Fraction fract1;
    Fraction fract2 (14, 21);
    Fraction fract3 (11, -8);
    Fraction fract4 (fract3);
    Fraction fract5(2,0);
    
    // Printing the object
    cout << "Printing four fractions after constructed: " << endl;
    cout << "fract1: ";
    fract1. print();
    cout << "fract2: ";
    fract2. print();
    cout << "fract3: ";
    fract3. print();
    cout << "fract4: ";
    fract4. print();
    cout << "fract5: ";
    fract5.print();
    
    // Using mutators
    cout << "Changing the first two fractions and printing them:";
    cout << endl;
    fract1.setNumer(4);
    cout << "fract1: ";
    fract1.print();
    fract2.setDenom(-5);
    cout << "fract2: ";
    fract2.print();
    
    // Using accessors
    cout << "Testing the changes in two fractions:" << endl;
    cout << "fract1 numerator: " << fract1.getNumer() << endl;
    cout << "fract2 denominator: " << fract2.getDenom() << endl;
    
    //testing problem3: multiplying fractions
    Fraction product;
    //fract1 = 1/2
    fract1.setNumer(1);
    fract1.setDenom(2);
    //fract2 = 2/3
    fract2.setNumer(2);
    fract2.setDenom(3);
    product = multiplyFract(fract1, fract2);
    cout << "product of fract1 and fract2: ";
    product.print();
    
    return 0;
}

/*
This function multiplies two fractions
@return reference of a fraction (fr1)
*/
Fraction& multiplyFract (Fraction& fr1, Fraction& fr2)
{
    int num = fr1.getNumer() * fr2.getNumer();
    int den = fr1.getDenom() * fr2.getDenom();
    fr1.setDenom(den);
    fr1.setNumer(num);
    return fr1;
}
