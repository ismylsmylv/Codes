#include<iostream>
#include<fstream>
using namespace std;
int main(){
fstream my_file("sample.txt", ios::out);
if (my_file.fail()){
    cout<<"Error! Unable to open file";
}
my_file<<"Hello There!";
my_file.close();
cout<<"Succesfully written to sample.txt";
return 0;
}