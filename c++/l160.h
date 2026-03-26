#pragma once
#include <iostream>
#include "ListNode.h"
using namespace std;

class Solution {
public:
	ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
		int lenA = 0, lenB = 0;
		ListNode* curA = headA;
		ListNode* curB = headB;
		while (curA)
		{
			curA = curA->next;
			lenA++;
		}
		while (curB)
		{
			curB = curB->next;
			lenB++;
		}
		curA = headA;
		curB = headB;

		if (lenA  < lenB)
		{
			swap(lenA, lenB);
			swap(curA, curB);
		}

		int offset = lenA - lenB;
		while (offset--)
		{
			curA = curA->next;
		}

		while (curA)
		{
			if (curA == curB)
			{
				return curA;
			}
			curA = curA->next;
			curB = curB->next;
		}
		return nullptr;
	}
};