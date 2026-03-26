#pragma once
#include <iostream>
#include <vector>
#include "ListNode.h"
using namespace std;



class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* pre = new ListNode;
        pre->next = head;
        ListNode* cur = pre;
        while (cur->next)
        {
            if (cur->next->val==val)
            {
                ListNode* temp = cur->next;
                cur->next = cur->next->next;
                delete temp;
            }
            else
            {
                cur = cur->next;
            }
        }
        head = pre->next;
        delete pre;
        return head;
    }
};