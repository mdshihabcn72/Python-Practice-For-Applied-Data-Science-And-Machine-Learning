//闰年判断（选做

#include <iostream>
using namespace std;

int main() {
    int year;
    
    cout << "请输入一个年份: ";
    cin >> year;
    
    // 使用逻辑运算符判断闰年
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        cout << year << " 是闰年" << endl;
    } else {
        cout << year << " 不是闰年" << endl;
    }
    
    return 0;
}