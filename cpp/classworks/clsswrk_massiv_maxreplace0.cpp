#include<iostream>
using namespace std;
int main()
{const int n=3;
int a[n][n], i, j, max;
cout<<"a massivini daxil edin";
for (i=0; i<n; i++)
for (j=0; j<n; j++)
cin>>a[i][j];
for(i=0; i<n; i++)
{
max=a[i][j];
for(j=0; j<n; j++)
if(a[i][j]>max)
max=a[i][j];
}

cout<<max<<" ";
for (i=0; i<n; i++){                //showing massiv
    for (j=0; j<n; j++)
    cout<<a[i][j];
}
return 0;
}

//      \o/
//       |      Ugh-oh, it isn't working
//      / \

//27.09.22  First massive is 2 dimensional, but equation (b[n]) is one. They both should have same size