# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.




# Getting the idea of linked list right first. 
# Linked list has 2 parts, the node and the series which is the actual list. 
# Lets consider them as two objects Node and Linkedlist. The node is gonna have a data part that holds the value and a next part which is a pointer to the next node. 
# The linked list has just a head part, and as we progress by mapping the node.next to another value.. the linkedList expands.

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        # Now that we've populated the new_node variable with the data using the constructor function of Node, we can append it as the head of the list if head is empty
        if self.head == None:
            self.head = new_node
            return
        # If head is not empty, we iterate to the next element and moving on till the last element in the list
        last_node = self.head
        # Until the last_node.next is None (this loop runs until last_node.next has a value)
        while last_node.next: 
            # we reassign the last_node.next to last_node
            last_node = last_node.next
        last_node.next = new_node


# Creation of a list and Adding a variable or a node to an existing list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        