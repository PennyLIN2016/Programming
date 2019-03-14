// Definition for singly-linked list.
 
function ListNode(val) {
    this.val = val;
    this.next = null;
  }
 
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs2 = function(head) {//faster than 88.13
    var pre = new ListNode(-1),tmp_pre = new ListNode(-1);
    pre.next = head;
    tmp_pre = pre;

    while(head!=null &&head.next!=null){
        var tmp= new ListNode(-1);
        tmp= head.next.next; 
        tmp_pre.next = head.next;
        head.next.next = head;
        head.next = tmp;
        tmp_pre = head;
        head = tmp;
    };
    return(pre.next)
};

var swapPairs1 = function(head) {// faster than 14.95%
    var pre = new ListNode(-1),tmp_pre = new ListNode(-1),tmp_node = new ListNode(-1);
    pre.next = head;
    tmp_pre = pre;
    var s = [];

    while(head!=null ){
        if(s.length==0){
            s.push(head);
            head= head.next;
        }else{
            tmp_pre.next = head;
            tmp_node = s.pop();
            tmp_node.next = head.next;
            tmp_pre = tmp_node;
            head.next = tmp_node;
            head = tmp_node.next;
        };
    };
    return(pre.next)
};

// input the links
var number1_1 = new ListNode(2),number1_2 = new ListNode(4),number1_3 = new ListNode(9),number1_4 = new ListNode(-1);
number1_1.next = number1_2;
number1_2.next = number1_3;
number1_3.next = number1_4

// get the sum
var node_re = null;
node_re = swapPairs(number1_1);
console.log(node_re.val);
// debug again the node_re is wrong. 
console.log('The end!');