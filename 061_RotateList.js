//Definition for singly-linked list.
function ListNode(val){
     this.val = val;
     this.next = null;
};

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    //Runtime: 72 ms, faster than 65.23% of JavaScript online submissions for Rotate List.
    //Memory Usage: 35.7 MB, less than 17.39% of JavaScript online submissions for Rotate List.
    if (head===null || head.next===null||k<=0){
        return(head);
    };
    var pre_head= head;
    var node_stack =[];
    while (head.next!=null){
        node_stack.push(head);
        head=head.next;
    };
    node_stack.push(head);
    var l= node_stack.length;
    k = k%l;
    if (k===0){
        return(pre_head);
    };
    node_stack[l-1].next= pre_head;
    node_stack[l-k-1].next = null;
    return(node_stack[l-k]);
};

var n1= new ListNode(1);
var n2= new ListNode(2);
var n3= new ListNode(3);
var n4= new ListNode(4);
var n5= new ListNode(5);
n1.next=n2;
//n2.next=n3;
//n3.next=n4;
//n4.next=n5;
var k=2;

console.log(rotateRight(n1,k).val);
console.log('-----------the end!----------------');

