    #include <iostream>
    #include <vector>
    #include <string>
    using namespace std;
    int main ()
    {
        string input1, input2;
        cin >> input1;
        cin >> input2;
     
        vector<int> vec1(input1.begin(), input1.end());
        vector<int> vec2(input2.begin(), input2.end());
        int lengthOfTheVectors = vec1.size();
     
        for (int i = 0; i < lengthOfTheVectors; i++)
        {
            int currentChar1 = vec1[i]-48;
            int currentChar2 = vec2[i]-48;
     
            if (currentChar1 == currentChar2)
                cout << '0';
            else
                cout << '1';
        };
    }