#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n,m; cin>>n>>m;
    int a[n];
    for(int i=0;i<n;i++)cin>>a[i];
    sort(a,a+n);
    int i=0,x,f=0;
    for(int j=0;j<m;j++)
    {
        cin>>x;
        int sum=0,c=0;
        while(sum<x){
            if(i==n){f=1;break;}
            sum+=a[i];
            i++;c++;
        }
        if(f==0)cout<<c<<" "<<sum<<endl;
        else cout<<"-1 -1"<<endl;
    }
    return 0;
}
