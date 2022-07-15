    #include <iostream>
    using namespace std;
    int x,k,a,counter=0,array[100];
    int main(){
        cin >>x>>k;
        for(int i=1;i<=x;i++){
            cin>>a;
            array[i]=a;
        };
        for(int j=1; j<=x;j++){
            if(array[j]>=array[k] && array[j]>0){
                counter++;
            }
        }
        cout << counter;
        return 0;
    }