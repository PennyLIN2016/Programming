//Definition for singly-linked list.
 
function ListNode(val) {
    this.val = val;
    this.next = null;
}
 
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {// faster than 5.02%
    var k = lists.length;
    if (k==0){
        return(null);
    };
    if (k==1){
        return(lists[0]);
    };
    var empty_n = 0;
    var head = new ListNode(-1),tail = new ListNode(-1);
    head.next = tail;

    while (empty_n<k){
        var i=0;
        var tmp_mix_val = Infinity,tmp_mix_pos=0;
        for(i=0;i<k;i++){
            if(lists[i]!=null && lists[i]!='O' && tmp_mix_val>lists[i].val){
                tmp_mix_val = lists[i].val;
                tmp_mix_pos = i
            };
            if (lists[i]==null){
                empty_n++;
                lists[i]='0';
            };
        };
        tail.next= lists[tmp_mix_pos];
        lists[tmp_mix_pos]= lists[tmp_mix_pos].next;
        if(empty_n<k){
            tail=tail.next;
        }else{
            tail.next= null;
        };
    };
    return(head.next.next)  
};


var number1_1 = new ListNode(2),number1_2 = new ListNode(2),number1_3 = new ListNode(9);
var number2_1 = new ListNode(1),number2_2 = new ListNode(6),number2_3 = new ListNode(7);
number1_1.next = number1_2;
number1_2.next = number1_3;
number2_1.next = number2_2;
number2_2.next = number2_3;

// get the sum
var node_re = null;

node_re = mergeKLists([number1_1,number2_1]);

console.log('The end!');