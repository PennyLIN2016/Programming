/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {

    var loop_in = 0;
    var re_list = [];
    while (loop_in < nums.length){
        var cur_index = nums.indexOf(target-nums[loop_in]);
        if (cur_index!= -1 && cur_index != loop_in ){
            re_list= [loop_in,cur_index];
            return re_list;
        }
        loop_in ++;

    }

    return re_list;
    
};

var list= [2, 6, 11, 15,7];
var tar= 9;

result= twoSum(list,tar);
console.log('the result is ' + result);