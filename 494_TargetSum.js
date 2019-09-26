/**
 * @param {number[]} nums
 * @param {number} S
 * @return {number}
 */
//Runtime: 220 ms, faster than 72.35% of JavaScript online submissions for Target Sum.
//Memory Usage: 51.5 MB, less than 100.00% of JavaScript online submissions for Target Sum.
var findTargetSumWays = function(nums, S){
    var l= nums.length;
    var dp= new Array(l+1);
    dp[0]={};
    dp[0]['0']=1;
    for(var i=0;i<l;i++){
        dp[i+1]= {};
        var keys= Object.keys(dp[i]);
        for(var j=0;j<keys.length;j++){
            var key_j=parseInt(keys[j]);
            if(dp[i+1].hasOwnProperty((key_j+nums[i]).toString())){
                dp[i+1][(key_j+nums[i]).toString()]+=dp[i][keys[j]];
            }else{
                dp[i+1][(key_j+nums[i]).toString()]=dp[i][keys[j]];
            };
            if(dp[i+1].hasOwnProperty((key_j-nums[i]).toString())){
                dp[i+1][(key_j-nums[i]).toString()]+=dp[i][keys[j]];
            }else{
                dp[i+1][(key_j-nums[i]).toString()]=dp[i][keys[j]];
            };
        };
    };

    if(dp[l].hasOwnProperty(S)){ return dp[l][S]};
    return 0
    
};

var A = [1, 1, 1, 1, 1];
var a= 3;

console.log(findTargetSumWays(A,a));
console.log('-----------the end!----------------');