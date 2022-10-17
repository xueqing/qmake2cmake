#include <iostream>

#include "secondlib.h"

using namespace std;

int main()
{
    cout << "Hello World!" << endl;
    Secondlib* pSecond = new Secondlib(333);
    delete pSecond;
    return 0;
}
