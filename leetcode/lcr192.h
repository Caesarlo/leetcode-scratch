#pragma once
#include <iostream>
using namespace std;


class Solution {
public:
	int myAtoi(string str) {
		int length = str.size();
		int i = 0;
		bool isNegative = false;
		while (true)
			if (str[i] == ' ')
				i++;
			else
				break;
		if (str[i] == '+')
		{
			i++;
		}
		else if (str[i] == '-')
		{
			i++;
			isNegative = true;
		}
		int index = i;
		int res = 0;
		while (true)
		{
			if(i>=length)
				break;
			if (str[i] >= '0' && str[i] <= '9')
			{
				if (res > INT_MAX / 10 || (res == INT_MAX / 10 && str[i] - '0' > 7))
					return isNegative ? INT_MIN : INT_MAX;
				res = res * 10 + (str[i] - '0');
				i++;
			}
			if (str[i] < '0' || str[i] > '9')
				break;
		}
		return isNegative ? -res : res;

	}
};