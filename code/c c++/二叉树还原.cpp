#include<stdio.h>
#include<string.h>
#include<stdlib.h>
typedef struct tree
{
	char Data;
	tree *left;
	tree *right;
}tree;
void reduction(char a[],char b[],tree *point)
{
	char first=a[0];
	point->Data=first;
	int i=0;
	while(b[i]!=first)
		i++;
	if(i==0)
	{
		point->left=NULL;
	}
	if(i!=0)
	{	
		tree *p;
		p=(tree*)malloc(sizeof(tree));
		p->Data=a[1];
		point->left=p;
		char preleft[100];
		char inoleft[100];
		int j=0;
		while(j!=i)
		{
			preleft[j]=a[j+1];
			j++;
		}
		int l=0;
		while(l!=i)
		{
			inoleft[l]=b[l];
			l++;
		}
		reduction(preleft,inoleft,p);
	}
	if(i==strlen(b)-1)
	{
		point->right=NULL;
	}
	if(i!=strlen(b)-1)
	{
		tree *q;
		q=(tree*)malloc(sizeof(tree));
		q->Data=a[i+1];
		point->right=q;
		char preright[100];
		char inoright[100];
		int k=0;
		while((k+i+1)!=strlen(a))
		{
			preright[k]=a[k+i+1];
			k++;
		}
		int o=0;
		while((o+i+1)!=strlen(b))
		{
			inoright[o]=b[o+i+1];
			o++;
		}
		reduction(preright,inoright,q);
	}
}
void LRD(tree *point)
{
	if(point->left!=NULL)
	{
		tree *next;
		next=(tree*)malloc(sizeof(tree));
		next=point->left;
		LRD(next);
	}
	if(point->right!=NULL)
	{
		tree *next;
		next=(tree*)malloc(sizeof(tree));
		next=point->right;
		LRD(next);
	}
	printf("%c",point->Data);
}
int main()
{
	tree *thetree;
	thetree=(tree*)malloc(sizeof(tree));
	char a[100];
	char b[100];
	scanf("%s %s",a,b);
	if(strlen(a)!=strlen(b))
	{
		printf("error");
	}
	else
	{
		reduction(a,b,thetree);
		LRD(thetree);
	}
	return 0;
}
