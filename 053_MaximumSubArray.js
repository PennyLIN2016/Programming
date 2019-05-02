/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    //Runtime: 64 ms, faster than 97.75% of JavaScript online submissions for Maximum Subarray.
    //Memory Usage: 35 MB, less than 85.60% of JavaScript online submissions for Maximum Subarray.
    var pre_max = 0;
    var cur_max = nums[0];
    for(var i=0;i<nums.length;i++){
        //the maximum including nums[i]
        pre_max= Math.max(pre_max+nums[i],nums[i]);
        cur_max = Math.max(pre_max,cur_max);
    };
    return(cur_max); 
};

var inputi = [-2,1,-3,4,-1,2,1,-5,4];
console.log(maxSubArray(inputi));
console.log('-----------the end!----------------');

