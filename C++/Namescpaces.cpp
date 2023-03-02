#include <iostream>

namespace first{
    int x = 1;
}
namespace second{
    int x = 2;
}

int main(){
    /* Namespace = Prevents name conflicts*/
using namespace first;

    int x = 0;

    std::cout << second::x;

    return 0;
}