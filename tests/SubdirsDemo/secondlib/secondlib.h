#ifndef SECONDLIB_H
#define SECONDLIB_H

#include "secondlib_global.h"
#include "firstlib.h"

class SECONDLIBSHARED_EXPORT Secondlib
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
