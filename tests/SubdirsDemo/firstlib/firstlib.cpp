#include "firstlib.h"

#include <iostream>

using namespace std;

Firstlib::Firstlib()
    : m_nNum(1)
{
    cout << "Firstlib(): m_nNum=" << m_nNum << endl;
}

Firstlib::Firstlib(int num)
    : m_nNum(num)
{
    cout << "Firstlib(int): m_nNum=" << m_nNum << endl;
}

Firstlib::~Firstlib()
{
    cout << "~Firstlib(): m_nNum=" << m_nNum << endl;
}
