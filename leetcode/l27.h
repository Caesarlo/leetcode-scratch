#pragma once
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	int removeElement(vector<int>& nums, int val) {
		int slow = 0;
		for (int fast = 0; fast < nums.size(); fast++) if (nums[fast] != val) nums[slow++] = nums[fast];
		return slow;
	}
};