// Input:
// Enter a Number: 22


#include <iostream>
using namespace std;

int main()
{
    int space = 0;
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    for (int i = 0; i < (n % 2 == 0 ? n / 2 : n / 2 + 1); i++)
    {
        for (int x = 0; x < space; x++)
        {
            cout << " ";
        }

        for (int j = space; j < n - space; j++)
        {
            cout << "*";
        }
        cout << endl;
        space++;
    }

    return 0;
}


// Output:
// Enter a Number: 22
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
//   1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
//     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
//       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
//         1 1 1 1 1 1 1 1 1 1 1 1 1 1
//           1 1 1 1 1 1 1 1 1 1 1 1
//             1 1 1 1 1 1 1 1 1 1
//               1 1 1 1 1 1 1 1
//                 1 1 1 1 1 1
//                   1 1 1 1
//                     1 1