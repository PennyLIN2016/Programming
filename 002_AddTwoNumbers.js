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
var addTwoNumbers = function(l1, l2) {
      var re_node = null, p_pre = null;

      flag = 0
      while (l1!=null | l2!=null)
      {

            if (l1===null){
                  re_node.next = l2;
                  break;
            }
            if (l2===null){
                  re_node.next = l1;
                  break;
            }
            if (re_node===null){
                  re_node = new ListNode((l1.val+l2.val+flag)%10);
                  p_pre = re_node;
            }else{
                  p1 = new ListNode((l1.val+l2.val+flag)%10);
                  p_pre.next = p1;
                  p_pre = p1;

            }
            if ((l1.val+l2.val+flag)>9){
                  flag = 1;
            }else{
                  flag = 0;
            };
            
            l1 = l1.next;
            l2 = l2.next;

      }

    return re_node
};

// input the links
var number1_1 = new ListNode(2),number1_2 = new ListNode(4),number1_3 = new ListNode(3);
var number2_1 = new ListNode(5),number2_2 = new ListNode(6),number2_3 = new ListNode(4);
number1_1.next = number1_2;
number1_2.next = number1_3;
number2_1.next = number2_2;
number2_2.next = number2_3;

// get the sum
var node_re = null;
node_re = addTwoNumbers(number1_1,number2_1);

// debug again the node_re is wrong. 
console.log('The sum is '+ node_re.next.next.val)


