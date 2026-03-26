#pragma once
#include <iostream>
#include <vector>
using namespace  std;



class Solution {
public:
	vector<int> spiralArray(vector<vector<int>>& array) {
		if (array.empty()) return {};
		int l = 0, t = 0, r = array[0].size() - 1, b = array.size() - 1;
		vector<int> result;
		while (true)
		{
			for (int i = l; i <= r; i++)
				result.push_back(array[t][i]);
			if (++t > b) break;;
			for (int i = t; i <= b; i++)
				result.push_back(array[i][r]);
			if (--r < l)break;
			for (int i = r; i >= l; i--)
				result.push_back(array[b][i]);
			if (--b < t)break;
			for (int i = b; i >= t; i--)
				result.push_back(array[i][l]);
			if (++l > r) break;
		}
		return result;
	}
};