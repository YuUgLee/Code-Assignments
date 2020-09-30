//Newton Bao
//Class (CECS 282-01)
//Project Name (Prog 1 – Solitaire Prime)// Due Date (09/14/2020)
//I certify that this program is my own original work.
//I did not copy any part of this program from
//any other source. I further certify that I typed each
//and every line of code in this program
#include <iostream>
#include <string>
#include "Card.h"
#include "Deck.h"
using namespace std;

int main() {
  int x=0;
  cout<<"Welcome to Solitaire Prime!"<<endl;
  cout<<"1) New Deck"<<endl;
  cout<<"2) Display Deck"<<endl;
  cout<<"3) Shuffle Deck"<<endl;
  cout<<"4) Play Solitaire Prime"<<endl;
  cout<<"5) Exit"<<endl;
  Deck d1;
  //while loop for each option in the menu
while (x!=5){
  cin >> x;
  if (x==1){
     d1.refreshDeck();
     cout<<"1) New Deck"<<endl;
  cout<<"2) Display Deck"<<endl;
  cout<<"3) Shuffle Deck"<<endl;
  cout<<"4) Play Solitaire Prime"<<endl;
  cout<<"5) Exit"<<endl;
  }
  else if (x==2){
     d1.showDeck();
     cout<<"1) New Deck"<<endl;
  cout<<"2) Display Deck"<<endl;
  cout<<"3) Shuffle Deck"<<endl;
  cout<<"4) Play Solitaire Prime"<<endl;
  cout<<"5) Exit"<<endl;
  cout<<endl;
  }
  else if (x==3){
     d1.shuffle();
     cout<<"1) New Deck"<<endl;
  cout<<"2) Display Deck"<<endl;
  cout<<"3) Shuffle Deck"<<endl;
  cout<<"4) Play Solitaire Prime"<<endl;
  cout<<"5) Exit"<<endl;
  
  }
  else if (x==4){

      d1.Solitaire();
      cout<<"1) New Deck"<<endl;
  cout<<"2) Display Deck"<<endl;
  cout<<"3) Shuffle Deck"<<endl;
  cout<<"4) Play Solitaire Prime"<<endl;
  cout<<"5) Exit"<<endl;
    
  }
}

}