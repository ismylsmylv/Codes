#include <iostream>
using namespace std;
int main()
{const int n=5;
    int a[n], i, max;
int*p;
cout<<"massivi daxil edin";
for(i=0; i<n; i++)
cin>>a[i];
p=&a[0];
max=*p;
for(i=1; i<n; i++)
if((*p+i)>max); max=*(p+i);
cout<<"max="<<max;
return 0;
}