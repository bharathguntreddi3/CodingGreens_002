#include<bits/stdc++.h>
using namespace std;

long a[100005];
void insertion(int n)
{
    if(n<=1)return ;
    int k=a[n-1],j=n-2;
    while(j>=0 and a[j]>k)
    {
        a[j+1]=a[j];j--;
    }
    a[j+1]=k;
}
int main(){
    int n; scanf("%d",&n);
    int size=0;
    for(int i=0;i<n;i++)
    {
       char c; int x; scanf(" %c%d",&c,&x);
       if(c=='a'){
              a[size]=x; size++; insertion(size);
       }
       else{
           if(size==0){printf("Wrong!\n"); continue;}
           int f=0;
           for(int j=0;j<size;j++)
           {
               if(a[j]==x){
                   f=1;
                   for(int k=j+1;k<size;k++)a[k-1]=a[k];
                   size--;
                   break;
               }
           }
           if(f==0){printf("Wrong!\n"); continue;}
       }
       if(size==0)printf("Wrong!\n");
       else if(size&1)printf("%ld\n",a[size/2]);
       else if(((a[size/2]+a[size/2-1])&1)==0)printf("%ld\n",(a[size/2]+a[size/2-1])/2);
       else printf("%.1lf\n",(a[size/2]+a[size/2-1])/2.0);
    }
}
