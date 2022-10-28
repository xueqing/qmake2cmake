#include "secondlib.h"

#include <iostream>

using namespace std;

Secondlib::Secondlib()
    : m_nNum(2)
    , m_pFirst(new Firstlib(2))
{
    cout << "Secondlib(): m_nNum=" << m_nNum << endl;
}

Secondlib::Secondlib(int num)
    : m_nNum(num)
    , m_pFirst(new Firstlib(num))
{
    cout << "Secondlib(int): m_nNum=" << m_nNum << endl;
}

Secondlib::~Secondlib()
{
    cout << "~Secondlib(): m_nNum=" << m_nNum << endl;
    if (m_pFirst)
    {
        delete m_pFirst;
        m_pFirst = nullptr;
    }
}
