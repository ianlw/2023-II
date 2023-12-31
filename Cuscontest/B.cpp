#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int te;
    cin >> te;
    while (te--){
        int n;
        cin >> n;
        vector<pair<int, string>> a(n);
        for(auto &[x,y]:a) cin >> x >>y;
        sort(a.begin(), a.end());
        for (auto [x,gg]:a)
            cout << gg << "\n";
    }
    return 0;
}
