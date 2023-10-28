#include<iostream>
using namespace std;

int main()
{   int n;
    cin>>n;
    int a=n/1000;  //minlik
    int b=n/100%10;  //yüzlük
    int c=n/10%10;  //onluq
    int d=n/1%10;  //təklik
    int e=(a+b+c+d);
    cout<<"e="<<e<<'\n';
    return 0;
}