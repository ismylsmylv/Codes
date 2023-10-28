#include <iostream>
using namespace std;
int main()
{
	setlocale(LC_ALL ,"Turkish");
	int n,m,i,j,max,x,y,sum=0,sum1=0;
	cout<<"Setirlerin sayýný daxil edin : ";
	cin>>n;
	cout<<"Sütünlarýn sayýný daxil edin : ";
	cin>>m;
	cout<<endl;
	int a[n][m];
	for(i=0;i<n;i++)
	{
		cout<<i+1<<". setirin elementlerini daxil edin : ";
		for(j=0;j<m;j++)
		{
			cin>>a[i][j];
		}
	}
	max=a[0][0];
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(a[i][j]>max)
			{
				max=a[i][j];
				x=i;
				y=j;
			}
		}
	}
	for(i=0;i<n;i++)
	{
		sum+=a[i][y];
	}
	for(j=0;j<m;j++)
	{
		sum1+=a[x][j];
	}
	cout<<endl<<"2D massivin maksimum elementi : "<<max<<endl<<endl;
	cout<<"Bu element "<<x+1<<". setirin "<<y+1<<". sütununda yerlesir ."<<endl<<endl;
	cout<<"Elementin yerleþdiyi sütundaký elementlerin cemi : "<<sum<<endl;
	cout<<"Elementin yerleþdiyi setirdeki elementlerin cemi : "<<sum1;
	return 0;
}
