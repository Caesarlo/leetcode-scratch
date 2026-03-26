#include <iostream>
#include <vector>
#include "l151.h"
#include <string>
using namespace std;

int main()
{
	Solution s;
	string str = "hello world";
	string pre = str.substr(0, 2);
	string post = str.substr(2, str.size() - 1);
	cout << pre << endl;
	cout << post << endl;

	return 0;
}