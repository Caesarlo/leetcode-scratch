#pragma once
#include <iostream>
#include <vector>
#include "ListNode.h"
using namespace std;



class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		ListNode* pre=NULL;
		ListNode* cur = head;
		ListNode* temp;
		while (cur != NULL)
		{
			temp = cur->next;
			cur->next = pre;
			pre = cur;
			cur = temp;
		}
		return pre->next;
	}
};