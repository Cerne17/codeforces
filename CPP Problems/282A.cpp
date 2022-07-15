    #include <iostream>
    using namespace std;
    int main(){
        int x,z=0;
        cin >> x;
        string a;
        for(int i=0;i<x;i++){
            cin >> a;
            if(a.find('++')!=-1){
                z++;
            }else{
                z--;
            }
        }
        cout << z;
        return 0;
    }