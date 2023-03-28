#include<bits/stdc++.h>
using namespace std;
void inorder(int a[],int i,int n)
{
    if(i<n and a[i]!=0)
    {
        inorder(a,2*i+1,n);
        printf("%d ",a[i]);
        inorder(a,2*i+2,n);
    }
}
int main()
{
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++)cin>>a[i];
    inorder(a,0,n);
}
