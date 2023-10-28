#include<iostream>
using namespace std;
int main()
{const int n=3;
int a[n][n], i, j, max;
int b[n];
cout<<"a massivini daxil edin";
for (i=0; i<n; i++)
for (j=0; j<n; j++)
cin>>a[i][j];
for(i=0; i<n; i++){
max=a[i][0];
for(j=0; j<n; j++)
if(a[i][j]>max)
max=a[i][j];
b[i]=max;}
for(i=0; i<n; i++)
cout<<b[i]<<" ";
return 0;
}