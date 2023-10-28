#include<iostream>
using namespace std;

int main()
{   int n;
    cin>>n;
    int a=n/10000; //on minlik
    int b=n/1000%10; //minlik
    int c=n/100%10;  //yüzlük
    int d=n/10%10;  //onluq
    int e=n/1%10;  //təklik
    cout<<"a="<<a<<'\n';
    cout<<"b="<<b<<'\n';
    cout<<"c="<<c<<'\n';
    cout<<"d="<<d<<'\n';
    cout<<"e="<<e<<'\n';
    return 0;
}