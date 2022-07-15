    #include <iostream>
    using namespace std;
    int main(){
        string a;
        char b;
        getline(cin, a);
        b=a[0];
        b=toupper(b);
        a[0]=b;
        cout << a;
        return 0;
    }