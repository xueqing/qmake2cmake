#include "firstlib.h"

#include <QtDebug>

Firstlib::Firstlib()
    : m_nNum(1)
{
    qDebug() << "Firstlib(): m_nNum=" << m_nNum;
}

Firstlib::Firstlib(int num)
    : m_nNum(num)
{
    qDebug() << "Firstlib(int): m_nNum=" << m_nNum;
}

Firstlib::~Firstlib()
{
    qDebug() << "~Firstlib(): m_nNum=" << m_nNum;
}
