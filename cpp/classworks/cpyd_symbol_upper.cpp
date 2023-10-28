#include<iostream>
#include<cstring>
#include<cctype>
using namespace std;
void ff(char s[])
{int i;
i=strlen(s);
for (i=0; i<1; i++)
toupper (s[i]);
}
int main()
{char u[]="blah blah";
ff (u);
cout<<u;
return 0;
}