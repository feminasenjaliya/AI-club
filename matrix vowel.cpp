#include<iostream>
using namespace std;
int main()
{
	char a[5][5];
	int n,m;
	cin>>n;
	cin>>m;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cin>>a[i][j];
		}
	}
		for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cout<<a[i][j]<<" ";
		}
		cout<<"\n";
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(a[i][j]=='a'||a[i][j]=='u'||a[i][j]=='o'||a[i][j]=='i'||a[i][j]=='e')
			{
				if(a[i+1][j]=='a'||a[i+1][j]=='u'||a[i+1][j]=='o'||a[i+1][j]=='i'||a[i+1][j]=='e')
				{
					if(a[i+1][j+1]=='a'||a[i+1][j+1]=='u'||a[i+1][j+1]=='o'||a[i+1][j+1]=='i'||a[i+1][j+1]=='e')
					{
						if(a[i][j+1]=='a'||a[i][j+1]=='u'||a[i][j+1]=='o'||a[i][j+1]=='i'||a[i][j+1]=='e')
						{
							cout<<i<<"-"<<j;
						}
					}
				}
			}
		}
	}
	return 0;
}
