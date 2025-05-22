#pragma once
#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
	string dynamicPassword(string password, int target) {
		return password.substr(target, password.size()) + password.substr(0, target);
	}
};