    #include <iostream>
    using namespace std;
    int main(){
        int a;
        cin >> a;
        if(a==2){
            cout << "NO";
        }else{
            a-=2;
            a=a%2;
            if(a==0){
                cout << "YES";
            }else{
                cout << "NO";
            }
        }
        return 0;
    }