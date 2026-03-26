#pragma once
#include <iostream>
using namespace std;




class MyLinkedList {
public:

	struct ListNode {
		int val;
		ListNode* next;
		ListNode() : val(0), next(nullptr) {}
		ListNode(int x) : val(x), next(nullptr) {}
		ListNode(int x, ListNode* next) : val(x), next(next) {}
	};
	 
	MyLinkedList() {
		this->_pre_node = new ListNode();
		_size = 0;
	}

	~MyLinkedList() {
		ListNode* cur = this->_pre_node;
		while (cur)
		{
			ListNode* temp = cur;
			cur = cur->next;
			delete temp;
		}
	}

	int get(int index) {
		if (index<0 || index>_size - 1)
			return -1;
		ListNode* cur = this->_pre_node->next;
		while (index--)
		{
			cur = cur->next;
		}
		return cur->val;
	}

	void addAtHead(int val) {
		ListNode* node = new ListNode(val);
		node->next = this->_pre_node->next;
		this->_pre_node->next = node;
		_size++;
	}

	void addAtTail(int val) {
		ListNode* node = new ListNode(val);
		ListNode* cur = this->_pre_node;
		while (cur->next)
		{
			cur = cur->next;
		}
		cur->next = node;
		_size++;

	}

	void addAtIndex(int index, int val) {
		if (index<0 || index>this->_size)
			return;
		ListNode* node = new ListNode(val);
		ListNode* cur = this->_pre_node;
		while (index--)
		{
			cur = cur->next;
		}
		node->next = cur->next;
		cur->next = node;
		_size++;

	}

	void deleteAtIndex(int index) {
		if (index<0 || index>this->_size - 1)
			return;
		ListNode* cur = this->_pre_node;
		while (index--)
		{
			cur = cur->next;
		}
		ListNode* temp = cur->next;
		cur->next = cur->next->next;
		delete temp;
		temp = nullptr;
		_size--;
	}

private:
	ListNode* _pre_node;
	int _size;

};

