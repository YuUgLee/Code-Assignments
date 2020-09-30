#include "Card.h"
#include "Deck.h"
#include <string>
#include <iostream>
using namespace std;
//Creates a standard deck
Deck :: Deck(){
  count=0;
  int num=0;
char suits[4]={'S','H','D','C'};
for (int s=0;s<4;s++){
  for (int n=1;n<14;n++){
    char a=(char)(n+'0');
    if (n==10){
      a='T';
    }
    else if (n==1){
      a='A';
    }
    else if (n==11){
      a='J';
    }
    else if (n==12){
      a='Q';
    }
    else if (n==13){
      a='K';
    }
    Card Card(a,suits[s]);
    storage[num++]=Card;
  }
}

}
//Creates a new deck
void Deck :: refreshDeck(){
  int num=0;
char suits[4]={'S','H','D','C'};
for (int s=0;s<4;s++){
  for (int n=1;n<14;n++){
    char a=(char)(n+'0');
    if (n==10){
      a='T';
    }
     else if (n==1){
      a='A';
    }
    else if (n==11){
      a='J';
    }
    else if (n==12){
      a='Q';
    }
    else if (n==13){
      a='K';
    }
    Card Card(a,suits[s]);
    storage[num++]=Card;
  }
}
}
//return number of cards
int Deck :: cardsLeft(){
return 52-count;
}
//deals card at the top
//returns card
Card Deck :: deal(){
    storage[count].showInitials();
    Card dealer=storage[count];
    // storage[count]=Card('\0','\0');
    count++;
    return dealer;

}
//shuffles deck
void Deck :: shuffle(){
 srand(time(0));
  for (int i = 0; i < 52; i++)
  {
    int index = (rand() % 52);

    Card temp = storage[index];
    storage[index] = storage[i];
    storage[i] = temp;
   
  }

}
void Deck :: showDeck(){
int num=0;
      for ( int i = 0; i < 4; i++ )
      {
         for ( int j = 1; j <= 13; j++ )
             storage[num++].showInitials();
             cout <<endl;
      }
}
//Runs Solitaire game
void Deck :: Solitaire(){
  int sum=0;
  int num=0;
  string s="";
  for (int i=0;i<52;i++){
        storage[i].showInitials();
        sum+=storage[i].getValue() ;
        count++;
        if (i==51 && Prime(sum)==1){
          cout<<"Prime: "<<sum<<endl;
          cout<<"Winner in "<<num<<" piles!"<<endl;
 
        }
      
        else if ((i==51 && Prime(sum)==0)){
          cout<<"Loser"<<endl;
        
        }
        else if (Prime(sum)==1){
          cout<<"Prime: "<<sum<<endl;
          sum=0;
          num++;
          
        }
  }
}
//Calculates if numbers are prime numbers
//returns value of 0 or 1
int Deck :: Prime(int total){
  int n=0;
  for (int i=2;i<=total/2;i++){
    if (total%i==0){
      return 0;
    }
    else{
      n=1;
      return 1;
    }
  }
  return n;
}