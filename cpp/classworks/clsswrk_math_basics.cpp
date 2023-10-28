#include<iostream>
using namespace std;

int main()
{
float x,y;
char kod;
    cout << "x,y-i daxil edin=";
    cin >>x>>y;
    cout << "kodu daxil edin=";
    cin >> kod;
switch (kod)
{
case '+': cout<<"x+y="<<x+y; break;
case '-': cout<<"x-y="<<x-y; break;
case '*': cout<<"x*y="<<x*y; break;
case '/': cout<<"x/y="<<x/y; break;
default:cout<<"bele emel yoxdur";
return 0;
}
}