#include<iostream>
using namespace std;
int main()
{int input [100], output [100], miqdar, i;
cout<<"Massivin element sayi daxil edin\n";
cin>>miqdar;
cout<<miqdar<<" element daxil edin\n";
for (i=0; i<miqdar; i++)
{cin>>input[i];}
for (i=0; i<miqdar; i++)
{output[i]=input[miqdar-i-1];}
cout<<"Chevrilmish massiv:\n ";
for(i=0; i<miqdar; i++)
{cout<<output[i]<<"";}
return 0;}