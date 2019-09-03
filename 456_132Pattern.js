/**
 * @param {number[]} nums
 * @return {boolean}
 */
//Runtime: 60 ms, faster than 91.55% of JavaScript online submissions for 132 Pattern.
//Memory Usage: 37.9 MB, less than 100.00% of JavaScript online submissions for 132 Pattern.
var find132pattern = function(nums) {
    if(nums===null || nums.length<3)return false;
    var third=Number.MIN_SAFE_INTEGER;
    var two = [];
    for(var i=nums.length-1;i>-1;i--)
    {
        if(nums[i]<third) return true;
        while(two!==[] && two[two.length-1]<nums[i])third=two.pop();
        two.push(nums[i]);
    }
    return false;
    
};
var inlist=[1, 5, 3, 4];
console.log(inlist);
console.log(find132pattern(inlist));
console.log('-----------the end!----------------');