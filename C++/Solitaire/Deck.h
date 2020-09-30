//guard
#ifndef DECK_H
#define DECK_H

class Deck{
  private:
    Card storage[52];
    int topIndex;
    int count;

  public:
    Deck();
    void refreshDeck();
    int cardsLeft();
    Card deal();
    void shuffle();
    void showDeck();
    void Solitaire();
    int Prime(int total);
    
};
#endif