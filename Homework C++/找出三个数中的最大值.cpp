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
    

   /* int arr[5] = {2,3,4,5,6};
    for (int i=0;i<5;i++){
        if(i==3){
            cout<<"找到了"<< arr[i]<<endl;
        }
        else{
            cout<<"没找到"<<endl;
        }
    }*/

    
    return 0;
}