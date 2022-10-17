#include "secondlib.h"

#include <QDebug>

Secondlib::Secondlib()
    : m_nNum(2)
    , m_pFirst(new Firstlib(2))
{
    qDebug() << "Secondlib(): m_nNum=" << m_nNum;
}

Secondlib::Secondlib(int num)
    : m_nNum(num)
    , m_pFirst(new Firstlib(num))
{
    qDebug() << "Secondlib(int): m_nNum=" << m_nNum;
}

Secondlib::~Secondlib()
{
    qDebug() << "~Secondlib(): m_nNum=" << m_nNum;
    if (m_pFirst)
    {
        delete m_pFirst;
        m_pFirst = nullptr;
    }
}
