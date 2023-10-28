#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int k, a[k],i;
	cout<<"massivin sayini daxil edin: ";
  cin>>k;
	for(i=0;i<k;i++)
	cin>>a[i];
    int min=a[0];
    int max=a[0];
    int indexMin=0;
    int indexMax=0;
    for(i=0;i<k;i++)
    {
     if(min<a[i])
        { 
         min=a[i];
         indexMin=i;
        }
       if(max<a[i])
        { 
         max=a[i];
         indexMax=i;
        }
    }
    a[indexMax]=a[indexMin]+a[indexMax];

    a[indexMin]=a[indexMax]-a[indexMin];

    a[indexMax]=a[indexMax]-a[indexMin];
    for(i=0;i<k;i++)
    cout<<a[i];
}
