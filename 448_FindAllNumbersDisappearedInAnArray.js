/**
 * @param {number[]} nums
 * @return {number[]}
 */
//Runtime: 100 ms, faster than 82.72% of JavaScript online submissions for Find All Numbers Disappeared in an Array.
//Memory Usage: 44 MB, less than 25.00% of JavaScript online submissions for Find All Numbers Disappeared in an Array
var findDisappearedNumbers = function(nums) {
    for(var i=0;i<nums.length;i++){
        if (nums[Math.abs(nums[i])-1]>0){
            nums[Math.abs(nums[i])-1]*=-1;
        };
    };
    var res=[];
    for(var j=0;j<nums.length;j++){
        if (nums[j]>0){
            res.push(j+1);
        };
    };
    return res;
};

var in_list = [4,3,2,7,8,2,3,1];
console.log(in_list);
console.log(findDisappearedNumbers(in_list));
console.log('-----------the end!----------------');