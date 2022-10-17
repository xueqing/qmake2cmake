#ifndef FIRSTLIB_H
#define FIRSTLIB_H

#include "firstlib_global.h"

class FIRSTLIBSHARED_EXPORT Firstlib
{

public:
    Firstlib();
    Firstlib(int num);
    ~Firstlib();

    void setNo(int num) { m_nNum = num;}

private:
    int m_nNum;
};

#endif // FIRSTLIB_H
