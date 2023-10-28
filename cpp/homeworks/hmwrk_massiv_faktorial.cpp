#include <iostream>
using namespace std;

int main() {
    int n;
    long double faktorial = 1.0;
    cout << "Eded daxil edin: ";
    cin >> n;
    if (n < 0)
        cout << "Menfi ola bilmez!";
    else {for(int i = 1; i <= n; ++i) {
            faktorial *= i;}
        cout << "Faktorial " << n << " = " << faktorial;    
    }return 0;}