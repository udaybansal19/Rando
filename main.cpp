#include <bits/stdc++.h>

using namespace std;

int itr=0;

double func(double x, double r) {

    return r*x*(1-x);

}

double rando(double ini, double r ) {

    double x = ini;

    for(int i=0;i<itr;i++){
        x = func(x,r);
        cout<<x<<endl;
    }


    return x;
}

int main() {

    cout << fixed << setprecision(6);

    itr = 10;
    cout<<rando(1,0.2);

    return 0;
}