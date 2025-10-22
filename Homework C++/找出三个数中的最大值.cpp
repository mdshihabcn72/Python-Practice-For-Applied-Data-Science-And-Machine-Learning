//找出三个数中的最大值

#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    double max;
    
    cout << "请输入三个数字: ";
    cin >> a >> b >> c;
    
    // 找出最大值
    max = a;
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    
    cout << "最大的数字是: " << max << endl;
    
    return 0;
}