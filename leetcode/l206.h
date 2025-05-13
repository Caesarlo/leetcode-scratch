#pragma once
#include <iostream>
#include <vector>
#include "ListNode.h"
using namespace std;


ListNode* reverse(ListNode* cur, ListNode* pre)
{
	if (cur == NULL)
		return pre;
	ListNode* temp = cur->next;
	cur->next = pre;
	return reverse(temp, cur);
}


class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		return reverse(head, NULL);
	}
};