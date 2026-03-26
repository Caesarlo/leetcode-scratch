#pragma once
#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
	bool validNumber(string s) {
		int i = 0;
		int length = s.size();
		while (true)
			if (s[i] == ' ')
			{
				i++;
				continue;
			}
			else
				break;
		bool _sign = false;
		if (s[i] == '-' || s[i] == '+')
		{
			i++;
			_sign = true;
		}
		while (true)
		{
			if(s[i]=='.')
		}

	}
};