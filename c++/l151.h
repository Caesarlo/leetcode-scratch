#pragma once
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

vector<string> string_split(string str, char* delim)
{
	vector<string> result;
	//stringstream ss(str);
	//string split;
	//while (getline(ss,split,delim))
	//{
	//	result.push_back(split);
	//}
	char* p = strtok((char*)str.c_str(), delim);
	while (p!=NULL)
	{
		result.push_back(p);
		p = strtok(NULL, delim);
	}
	return result;
}


class Solution {
public:
	string reverseMessage(string message) {
		vector<string> words;
		string res="";
		char delim = ' ';
		words = string_split(message, &delim);
		for (int i = words.size() - 1; i >= 0; i--)
		{
			res += words[i];
			if (i != 0)
			{
				res += " ";
			}
		}
		return res;
	}
};