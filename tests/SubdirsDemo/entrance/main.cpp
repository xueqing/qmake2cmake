#include <iostream>

#include "secondlib.h"
#include "json11.hpp"

using namespace std;
using namespace json11;

void testJson11()
{
    const string simple_test =
        R"({"k1":"v1", "k2":42, "k3":["a",123,true,false,null]})";

    string err;
    const auto json = Json::parse(simple_test, err);

    std::cout << "k1: " << json["k1"].string_value() << "\n";
    std::cout << "k3: " << json["k3"].dump() << "\n";
}

int main()
{
    cout << "Hello World!" << endl;
    Secondlib* pSecond = new Secondlib(333);
    delete pSecond;
    testJson11();
    return 0;
}
