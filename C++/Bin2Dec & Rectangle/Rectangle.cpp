/**
This class includes the behaviors for the Rectangle object
*/

#include "Rectangle.h"

/**
Constructor for Rectangle that initially sets width and height to 1
*/
Rectangle :: Rectangle()
{
  width = 1;
  height = 1;
}

/**
Overloaded Constructor that sets height and width to the specified values
*/
Rectangle :: Rectangle(double w, double h)
{
  width = w;
  height = h;
}

/**
Calculates the area of the rectangle
@return area
*/
double Rectangle :: getArea(double w, double h)
{
  return w * h;
}

/**
Calculates the perimeter of the rectangle
@return perimeter
*/
double Rectangle :: getPerimeter(double w, double h)
{
  return (2*w) + (2*h);
}

/**
Accessor for width
@return width
*/
double Rectangle :: getWidth() const
{
  return width;
}

/**
Mutator for width
@param w width of rectangle
*/
void Rectangle :: setWidth(double w)
{
  width = w;
}

/**
Accessor for height
@return height
*/
double Rectangle :: getHeight() const
{
  return height;
}

/**
Mutator for height
@param h height of rectangle
*/
void Rectangle :: setHeight(double h)
{
  height = h;
}