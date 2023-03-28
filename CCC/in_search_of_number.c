#include <stdio.h>
#include <string.h>

int main() {
    char N[20];
    scanf("%s", N);
    int n = strlen(N);
    int i = n-2;
    while(i>=0 && N[i]>=N[i+1]){
        i--;
    }
    if(i==-1){
        printf("-1");
    }
    else{
        int m_ind = i+1;
        for (int j=j+2;j<n;j++){
            if(N[j]>N[i] && N[j]<N[m_ind]){
                m_ind = j;
            }
        }
        char t=N[m_ind];N[m_ind]=N[i];N[i]=t;
        int l=i+1, k=n-1;
        while(l<k){
            char t=N[l];N[l]=N[k];N[k]=t;l++;k--;
        }
        printf("%s", N);
    }
    return 0;
}
