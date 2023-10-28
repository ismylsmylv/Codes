#include<iostream>
using namespace std;
const int n=5;
void daxil(int mat[n])
{int i;
for (i=0; i<n; i++)
cin>>mat[i];}
void print(int mat[n])
{int i;
for(i=0; i<n; i++)
cout<<"mat["<<i<<"]="<<mat[i]<<" ";}
int main()
{int a[n], b[n], c[n];
    daxil (a); print(a);
    daxil (b); print(b);
    daxil (c); print(c);
return 1;
}