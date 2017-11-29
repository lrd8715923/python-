#include<stdio.h>
void re(int **m,int r[],int i,int j,int x);
void martix(int row[],int col[],int n);
int main()
{
	int n;
	scanf("%d",&n);
	int row[n];
	int col[n];
	int i;
	for(i=0;i<n;i++)
	{
		scanf("%d",&row[i]);
	}
	for(i=0;i<n;i++)
	{
		scanf("%d",&col[i]);
	}
	martix(row,col,n);
	return 0;
}
void martix(int row[],int col[],int n)
{
	int r[n+2];
	int i;
	r[1]=row[0];
	r[2]=col[0];
	for(i=3;i<n+2;i++)
	{
		r[i]=col[i-2];
	}
	int m[n+1][n+1];
	int j;
	for(i=0;i<n+1;i++)
	{
		for(j=0;j<n+1;j++)
		{
			if(i==j)
			{
				m[i][j]=0;
			}
			else
			{
				m[i][j]=-1;
			}
		}
	}
	int x=n+1;
	re((int**)m,r,1,n,x);
	printf("%d",m[1][n]);
}
void re(int **m,int r[],int i,int j,int x)
{
	int k; 
	for(k=i;k<j;k++)
	{
		if(*((int *)m+x*(k+1)+j)==-1)//a[i][j]=*((int *)a+x*i+j)
		{
			re(m,r,k+1,j,x);
		}
		if(*((int *)m+x*i+k)==-1)
		{
			re(m,r,i,k,x);
		}
		if( (*((int *)m+x*i+j)>*((int *)m+x*i+k)+*((int *)m+x*(k+1)+j)+r[i]*r[k+1]*r[j+1])||(*((int *)m+x*i+j))==-1)
			*((int *)m+x*i+j)=*((int *)m+x*i+k)+*((int *)m+x*(k+1)+j)+r[i]*r[k+1]*r[j+1];
	}
}
//4 35 40 20 10 40 20 10 15
