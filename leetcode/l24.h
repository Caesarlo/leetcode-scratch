#pragma once
#include <iostream>
#include "ListNode.h"
using namespace std;


class Solution1 {
public:
	ListNode* swapPairs(ListNode* head) {
		ListNode* dummy_head = new ListNode;
		dummy_head->next = head;
		ListNode* cur = dummy_head;
		while (cur->next != nullptr && cur->next->next != nullptr)
		{
			ListNode* tmp = cur->next;
			ListNode* tmp1 = cur->next->next->next;

			cur->next = cur->next->next;
			cur->next->next = tmp;
			cur->next->next->next = tmp1;

			cur = cur->next->next;
		}
		ListNode* result = dummy_head->next;
		delete dummy_head;
		return result;
	}
};


class Solution {
public:
	ListNode* swapPairs(ListNode* head) {
		if (!head || !head->next)
			return head;
		ListNode* newHead = head->next;
		head->next = swapPairs(newHead->next);
		newHead->next = head;
		return newHead;
	}
};