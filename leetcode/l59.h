#pragma once
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
	vector<vector<int>> generateMatrix(int n) {
		vector<vector<int>> nums(n, vector<int>(n, 0));
		int start_x = 0, start_y = 0;
		int offset = 1;
		int count = 1;
		int mid = n / 2;
		int loop = n / 2;
		int i, j;
		while (loop--)
		{
			i = start_x;
			j = start_y;
			for (; j < n - offset; j++)
				nums[start_x][j] = count++;
			for (; i < n - offset; i++)
				nums[i][j] = count++;
			for (; j > start_y; j--)
				nums[i][j] = count++;
			for (; i > start_x; i--)
				nums[i][j] = count++;
			offset++;
			start_x++;
			start_y++;	
		}
		if (n % 2 != 0)
			nums[mid][mid] = count;
		return nums;
	}
};