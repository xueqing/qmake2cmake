#ifndef SECONDLIB_H
#define SECONDLIB_H

#include "firstlib.h"

class Secondlib
{

public:
    Secondlib();
    Secondlib(int num);
    ~Secondlib();

private:
    int m_nNum;
    Firstlib* m_pFirst;
};

#endif // SECONDLIB_H
