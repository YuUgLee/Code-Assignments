#include "Card.h"
#include <iostream>
#include <string>
using namespace std;
//Blank Card
Card :: Card()
{
  rank='\0';
  suit='\0';

}
//Overload constructor
//Defines card
Card :: Card(char r, char s){
this->rank=r;
this->suit=s;
}
//Sets value for a blank card
void Card :: setCard(char r, char s){
this->rank=r;
this->suit=s;
  }
//Get value of Card
//@return integer value
int Card ::getValue(){
int num;
if (this->rank=='A'){
  num=1;
}
else if (rank=='T'){
  num=10;
}
else if (rank=='J' || rank=='K'|| rank=='Q'){
  num=10;
}
else if(rank=='1'){
  num=1;
}
else if (rank=='2'){
  num=2;
}
else if (rank=='3'){
  num=3;
}
else if (rank=='4'){
  num=4;
}
else if (rank=='5'){
  num=5;
}
else if (rank=='6'){
  num=6;
}
else if (rank=='7'){
  num=7;
}
else if (rank=='8'){
  num=8;
}
else if (rank=='9'){
  num=9;
}
return num;
}
//shows card details
void Card ::showCard(){
  string s="";
  string r="";
if (suit=='S'){
  s=" Spade";
}
else if (suit=='D'){
  s=" Diamond";  
}
else if (suit=='H'){
  s=" Heart";
}
else if (suit=='C'){
  s=" Club";
}

if (rank=='1'){
  r="Ace of";
}
else if (rank=='2'){
  r="Two of";
}
else if (rank=='3'){
  r="Three of";
}
else if (rank=='4'){
  r="Four of";
}
else if (rank=='5'){
  r="Five of";
}
else if (rank=='6'){
  r="Six of";
}
else if (rank=='7'){
  r="Seven of";
}
else if (rank=='8'){
  r="Eight of";
}
else if (rank=='9'){
  r="Nine of";
}
else if (rank=='T'){
  r="Ten of";
}
else if (rank=='J'){
  r="Jack of";
}
else if (rank=='Q'){
  r="Queen of";
}
else if (rank=='K'){
  r="King of";
}
else if (rank=='A'){
  r="Ace of";
}
  r+=s;
cout << r <<":" <<rank<<suit <<endl;
  }
//shows initial of card
void Card :: showInitials(){
  cout << rank << suit<<", ";
  
}