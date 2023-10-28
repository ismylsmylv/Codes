#include <iostream>
using namespace std;
#define k 100;
int main()
{int i, n, j, m, k, massiv[i];
for(i=0;i<n;i++)
{		
for(j=i+1;j<n;j++)
{
if(massiv[i]>massiv[j])
{m  =massiv[i];
massiv[i]=massiv[j];
massiv[j]=m;}
}
}
cout<<"Sorted (Ascending Order) massivay elements:"<<endl;
for(i=0;i<n;i++)
cout<<massiv[i]<<"\t";
cout<<endl;
return 0;}