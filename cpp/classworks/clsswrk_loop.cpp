#include<iostream>
using namespace std;
int main()
{int a[6], i;
int *P;
P=&a[0];
for(i=0; i=6; i++)
cout<<P+i<<'\n';
return 0;}