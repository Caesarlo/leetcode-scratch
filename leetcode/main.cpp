#include <iostream>
#include <vector>
#include "l59.h"
using namespace std;

int main()
{
	Solution s;
	int n = 3;
	vector<vector<int>> res(n, vector<int>(n, 0));
	res=s.generateMatrix(n);
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		{
			cout << res[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}