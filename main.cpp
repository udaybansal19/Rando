#include <bits/stdc++.h>

using namespace std;

long long int itr=0;

long double func(long double x,long double r) {

    return r*x*(1-x);

}

long double rando(long double ini,long double r,int view ) {

    long double x = ini;

    for(long long int i=0;i<itr;i++){
        x = func(x,r);
    }

    for(int i=0;i<view;i++){
        x = func(x,r);
        cout<<x<<endl;
    }

    return x;
}

int main() {

    itr = 1000;
    long double x = 0.2;
    long double r = 3.545;
    int display = 18;
    cout<<"Using logistics equation\n";
    cout<<"Initial Values: r: "<<r<<"  x: "<<x<<endl;
    cout<<"Number of iterations: "<<itr<<endl;
    cout << fixed << setprecision(6);
    rando(x,r,display);

    return 0;
}