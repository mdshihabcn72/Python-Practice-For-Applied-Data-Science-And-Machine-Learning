//BMI计算与分类
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    /*double height, weight, bmi;
    
    cout << "请输入您的身高（米）: ";
    cin >> height;
    
    cout << "请输入您的体重（千克）: ";
    cin >> weight;
    
    // 计算BMI
    bmi = weight / (height * height);
    
    cout << fixed << setprecision(2);
    cout << "您的BMI是: " << bmi << endl;
    
    // BMI分类
    if (bmi < 18.5) {
        cout << "分类: 体重过轻" << endl;
    } else if (bmi >= 18.5 && bmi < 24) {
        cout << "分类: 正常范围" << endl;
    } else if (bmi >= 24 && bmi < 28) {
        cout << "分类: 超重" << endl;
    } else {
        cout << "分类: 肥胖" << endl;
    }*/

    double t,p,w,s;
    cout<<"Input Weight :"<< endl;
    cin>>w;
    cout<<"Input distance :"<<endl;
    cin>>s;
    if (s<100) p=30;
    else if (s<200) p= 27.5;
    else if (s<300) p= 25;
    else if (s<400) p =22.5;
    else p =20;
    t = p*w*s;
    cout<<"The cost is :"<<t<<"$"<<endl;
    
    return 0;
}