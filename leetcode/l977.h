#pragma once
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> sortedSquares(vector<int>& nums) {
		int left = 0, right = nums.size() - 1;
		int k = nums.size() - 1;
		vector<int> result(nums.size());
		for (int i = 0, j = nums.size() - 1; i <= j; )
		{
			if (abs(nums[i]) > abs(nums[j]))
			{
				result[k--] = nums[i] * nums[i];
				i++;
			}
			else
			{
				result[k--] = nums[j] * nums[j];
				j--;
			}
		}
		return result;
	}
};