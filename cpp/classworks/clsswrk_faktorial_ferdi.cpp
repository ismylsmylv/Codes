#include<iostream>
using namespace std;
int faktor(int n)
{int P, i;
P=1;
for(i=1; i<=n; i++)
P=P*i;
return P;}
int main()
{int k,x,a;
float t;
cout<<"a, x, k daxil edin";
cin>>a>>x>>k;
t=(faktor(k)+faktor(5)+faktor(x))/(faktor(a)+faktor(7));
cout<<t;
return 0;
}