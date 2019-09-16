/**
 * @param {number[]} nums
 * @return {number}
 */
//Runtime: 64 ms, faster than 86.08% of JavaScript online submissions for Total Hamming Distance.
//Memory Usage: 37.4 MB, less than 100.00% of JavaScript online submissions for Total Hamming Distance.
var totalHammingDistance = function(nums) {
    var res=0;
    for(var i=0;i<32;i++){
        var count=0;
        for(j=0;j<nums.length;j++){
            count+=(nums[j]>>i)&1
        };
        res+=count*(nums.length-count);
    }
    return res;
    
};
var inlist=[4,14,2];
//console.log(inlist);
console.log(totalHammingDistance(inlist));
console.log('-----------the end!----------------');