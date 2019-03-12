//Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
};

/**
* @param {ListNode} head
* @param {number} n
* @return {ListNode}
*/
var removeNthFromEnd = function(head, n) {
    var pre = new ListNode(-1);
    pre.next = head;
    var fast = new ListNode(0),slow = new ListNode(0);
    fast = pre;
    slow = pre;
    while(n>0 && fast!==null){
        fast=fast.next;
        n--;
    };
    while(fast.next!==null && slow.next!==null){
        fast=fast.next;
        slow = slow.next
    };
    slow.next= slow.next.next;

    return(pre.next);

};



// input the links
var number1_1 = new ListNode(1),number1_2 = new ListNode(2),number1_3 = new ListNode(3),number1_4 = new ListNode(4),number1_5 = new ListNode(5);
number1_1.next = number1_2;
number1_2.next = number1_3;
number1_3.next = number1_4;
number1_4.next = number1_5;


// get the sum
var node_re = null;
node_re = removeNthFromEnd(number1_1,2);
