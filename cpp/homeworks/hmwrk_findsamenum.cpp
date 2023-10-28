#include <iostream>
using namespace std;
int main() {
int arr[] = {23, 123, 65, 3, 23, 98, 3, -5 ,23};
int n = sizeof(arr)/sizeof(arr[0]);
int tekrar[n];
int count = 0;
for (int i = 0; i < n; i++) {
    for (int j = i+1; j < n; j++) {
        if (arr[i] == arr[j]) {
            bool added = false;
    for (int k = 0; k < count; k++) {
        if (arr[i] == tekrar[k]) {
            added = true;
            break;}}
if (!added) {
tekrar[count++] = arr[i];
}
}
}
}
    cout << "Tekrar elementler: ";
    for (int i = 0; i < count; i++) {
        cout << tekrar[i] << " ";
    }
    return 0;
}
