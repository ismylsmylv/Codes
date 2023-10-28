//a massivinde sondan bashlayaraq qiymetleri deyish
#include<iostream>
using namespace std;
int main()
{const int n=10;
int a[n], i,c;
for (i=0; i<n; i++)
cin>>a[i];
for (i=0; i<n/2; i++)
c=a[n-i-1];
a[i]=a[n-i-1];
a[i]=c;
for(i=0; i<n;i++)
cout<<a[i]<<" ";
return 0;
}
