/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    //Runtime: 80 ms, faster than 89.85% of JavaScript online submissions for Permutations II.
    //Memory Usage: 37.2 MB, less than 82.86% of JavaScript online submissions for Permutations II.
    if(nums.length<1){
        return([]);
    };
    var subPer= function(r,nums,cur_path,visited_set){
        if(cur_path.length === nums.length){
            // must use a new list address and make sure the new list is a list ,not string.
            r.push(cur_path.slice());
            return;
        };
        var i;
        for(i=0;i<nums.length;i++){
            if(i>0 && nums[i]===nums[i-1] && visited_set[i-1]===1){
                visited_set[i]==1;
                continue;
            };
            if (visited_set[i] === undefined){
                visited_set[i]= 1;
                cur_path.push(nums[i]);
                subPer(r,nums,cur_path,visited_set);
                cur_path.pop();
                visited_set[i] = undefined;
            };
        };
        return;
    };

    nums.sort(function(a,b){return(a-b)});
    var r=[];
    subPer(r,nums,[],{});
    return(r);
};

var inputi = [1,1,3,5,3,1];
var r = permuteUnique(inputi);
console.log(r);
console.log('-----------the end!----------------');

