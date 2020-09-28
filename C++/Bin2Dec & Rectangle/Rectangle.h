/**
Header file for Rectangle
*/

#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle
{
  private:
    /**
    Represents the width of the rectangle
    */
    double width;
    /**
    Represents the height of the rectangle
    */
    double height;
  public:
    /**
    Constructors
    */
    Rectangle();
    Rectangle(double w, double h);

    /**
    Behaviors for Rectangle
    */
    double getArea(double w, double h);
    double getPerimeter(double w, double h);
    double getWidth() const; 
    void setWidth(double w);
    double getHeight() const;
    void setHeight(double h);
};
#endif