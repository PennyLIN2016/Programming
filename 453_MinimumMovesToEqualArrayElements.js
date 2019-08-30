/**
 * @param {number[]} nums
 * @return {number}
 */
//Runtime: 60 ms, faster than 87.70% of JavaScript online submissions for Minimum Moves to Equal Array Elements.
//Memory Usage: 37.5 MB, less than 100.00% of JavaScript online submissions for Minimum Moves to Equal Array Elements.
var minMoves = function(nums) {
    var minVal=Number.MAX_SAFE_INTEGER,sumVal=0;
    for(var i=0;i<nums.length;i++){
        sumVal+=nums[i];
        minVal=Math.min(minVal,nums[i]);
    };
    return sumVal-nums.length*minVal;
};

var in_list =[1,2,3];
console.log(in_list);
console.log(minMoves(in_list));
console.log('-----------the end!----------------');