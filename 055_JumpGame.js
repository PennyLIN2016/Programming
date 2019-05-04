/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    //Runtime: 60 ms, faster than 100.00% of JavaScript online submissions for Jump Game.
    //Memory Usage: 35.6 MB, less than 97.30% of JavaScript online submissions for Jump Game.
    if(nums.length<=1){
        return(true);
    };
    var get_i = 0;
    //make sure the i is reachable.i <= get_i
    for(var i=0;i<nums.length && i<=get_i;i++){
        get_i = Math.max(i+nums[i],get_i);
    };
    if(get_i>=nums.length-1){
        return(true);
    }else{
        return(false);
    };   
};
var inputi = [3,2,1,0,4];
console.log(canJump(inputi));
console.log('-----------the end!----------------');

