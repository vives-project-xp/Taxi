#include <iostream>

int main(){

    /* The constant keyword specifies that a variable's value
    is constant, it tells the compiler to prevent 
    anything from modifying it*/

    const double PI = 3.14159;
    PI = 420.69 // because of the const keyword the value wont change
    double radius = 10; 
    double circ = 2 * pi * radius;

    std::cout << circ << "cm" <<std::endl;
    return 0;
}