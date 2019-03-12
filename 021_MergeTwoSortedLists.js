/**
 * Definition for singly-linked list.
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}
 
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var head= new ListNode(-1),pre= new ListNode(-1)
    pre = head;
    
    while(l1!=null && l2!=null){
        if(l1.val>l2.val){
            if (head.next==null){
                head.next= l2;
            };
            pre.next=l2;
            pre=pre.next
            l2=l2.next;
        }else{
            if (head.next==null){
                head.next= l1;
            }; 
            pre.next= l1;
            pre=pre.next
            l1=l1.next;
        };
    };
    if(l1!=null){pre.next=l1};
    if(l2!=null){pre.next=l2};
    return(head.next)

};


// input the links
var number1_1 = new ListNode(2),number1_2 = new ListNode(2),number1_3 = new ListNode(9);
var number2_1 = new ListNode(1),number2_2 = new ListNode(6),number2_3 = new ListNode(7);
number1_1.next = number1_2;
number1_2.next = number1_3;
number2_1.next = number2_2;
number2_2.next = number2_3;

// get the sum
var node_re = null;
node_re = mergeTwoLists(number1_1,number2_1);

// debug again the node_re is wrong. 
console.log('The number is '+ node_re.val);