#include <iostream>
using namespace std;

int main() {
    int choice;
    
    do {
        cout << "\n=== Menu ===" << endl;
        cout << "1. Check Balance" << endl;
        cout << "2. Deposit Money" << endl;
        cout << "3. Withdraw Money" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch(choice) {
            case 1:
                cout << "Your balance: $1000" << endl;
                break;
            case 2:
                cout << "Money deposited!" << endl;
                break;
            case 3:
                cout << "Money withdrawn!" << endl;
                break;
            case 4:
                cout << "Thank you for banking with us!" << endl;
                break;
            default:
                cout << "Invalid choice! Try again." << endl;
        }
    } while (choice != 4);  // 4 press না করা পর্যন্ত continue করবে
    
    return 0;
}