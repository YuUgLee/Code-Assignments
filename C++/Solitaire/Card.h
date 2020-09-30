//guard
#ifndef CARD_H
#define CARD_H
class Card{
public:
  Card();
  Card(char r, char s);
  void setCard(char r, char s);
  int getValue();
  void showCard();
  void showInitials();
private:
char rank;
char suit;
};

#endif