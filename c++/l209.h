#pragma once
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
	int minSubArrayLen(int target, vector<int>& nums) {
		int i = 0, subL = 0, sum = 0;
		int result = INT_MAX;
		for (int j = 0; j < nums.size(); j++)
		{
			sum += nums[j];
			while (sum >= target)
			{
				subL = j - i + 1;
				result = min(result, subL);
				sum -= nums[i];
				i++;
			}
		}

		return result == INT_MAX ? 0 : result;
	}
};