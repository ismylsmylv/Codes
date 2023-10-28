#include<iostream>
using namespace std;

int main()
{ float a,b,c;
cout<<"a,b,c-ni daxil et";
cin>>a>>b>>c;
if(a<b+c&b<a+c&c<a+b)
cout<<"qurmaq olar";
else cout<<"qurmaq olmaz";
return 0;
}