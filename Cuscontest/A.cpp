#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(){
    int casos;
    cin >> casos;
    while (casos--) {
    int n;
    cin >> n;
    int suma = n*(n+1)/2;
    for (int i = 0; i < n-1; i++) {
        int x; cin >> x;
        suma -= x;
    }
    cout << suma << "\n";
    }
    return 0;
}
