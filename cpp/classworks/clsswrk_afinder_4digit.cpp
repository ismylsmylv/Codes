#include<iostream>
using namespace std;

int main()
{   int n;
    cin>>n;
    int a=n/1000;
    int b=n/100%10;
    int c=n/10%10;
    int d=n/1%10;
    cout<<"a="<<a<<'\n';
    cout<<"b="<<b<<'\n';
    cout<<"c="<<c<<'\n';
    cout<<"d="<<d<<'\n';
    return 0;
}