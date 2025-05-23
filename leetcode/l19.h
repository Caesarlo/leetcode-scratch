#pragma once
#include <iostream>
#include "ListNode.h"
using namespace std;

class Solution {
public:
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		ListNode* dummy_head = new ListNode(0);
		dummy_head->next = head;
		ListNode* fast = dummy_head;
		ListNode* slow = dummy_head;
		while (n-- && fast != NULL)
		{
			fast = fast->next;
		}
		fast = fast->next;
		while (fast != NULL)
		{
			fast = fast->next;
			slow = slow->next;
		}
		//slow->next = slow->next->next;
		ListNode* tmp = slow->next;
		slow->next = slow->next->next;
		delete tmp;
		return dummy_head->next;
	}
};