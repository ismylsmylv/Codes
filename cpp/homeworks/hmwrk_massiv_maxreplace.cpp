#include <iostream>
using namespace std;
int main() {
  int i, n;
  float massiv[100];
  cout << "element sayi daxil edin: ";
  cin >> n;
  cout << endl;
  for(i = 0; i < n; ++i) {
    cout << "elementleri daxil edin " << i + 1 << " : ";
    cin >> massiv[i];
  }
  for(i = 0;i < n; ++i) {
    if(massiv[0] < massiv[i])
      massiv[0] = massiv[i];
  }
cout << endl << "maksimum = " << massiv[0];
massiv[0]=2022;
cout<<" deyishmish => "<<massiv[0];
  return 0;
}