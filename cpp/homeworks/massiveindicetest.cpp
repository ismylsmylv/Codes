#include <iostream>
using namespace std;
int main()
{const int n=5;
    int n, a[n], i, max;
int*p;
cout<<"massivi daxil edin";
for(i=0; i<n; i++)
cin>>a[i];
p=&a[0];
for(i=1; i<n; i++); max=*p;
if((*p+i)>max; max=*(p+i));
for(i=0; i<n; i++)
cout<<p+i<<" ";
return 0;
}