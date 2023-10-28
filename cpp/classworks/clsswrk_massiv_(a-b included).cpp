#include<iostream>
using namespace std;
int main()
{const int n=3;
int a[n][n], i, j;
int a, b, say=0;
cout<<"massivi daxil edin";
for(i=0; i<n; i++)
for(j=0; j<n; j++)
cin>>a>>b;
for(i=0; i<n; i++)
for(j=0; j<n; j++)
if (a[i][j]>=a&&a[i][j]<b)
say=say+1;
cout<<say;
return 0;
}