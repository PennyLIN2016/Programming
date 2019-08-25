/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    //Runtime: 108 ms, faster than 64.47% of JavaScript online submissions for Find All Duplicates in an Array.
    //Memory Usage: 43.9 MB, less than 50.00% of JavaScript online submissions for Find All Duplicates in an Array.
    var res=[];
    nums.forEach(function(num){
        var value= Math.abs(num)-1;
        if (nums[value]<0){
            res.push((value+1));
        };
        nums[value]=-nums[value]
    });
    return(res);
};

var inputi =[4,3,2,7,8,2,3,1];

console.log(findDuplicates(inputi));
console.log('-----------the end!----------------');

