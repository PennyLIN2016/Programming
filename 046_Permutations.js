/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    //Runtime: 72 ms, faster than 88.99% of JavaScript online submissions for Permutations.
    //Memory Usage: 36 MB, less than 86.61% of JavaScript online submissions for Permutations.
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
    var r=[];
    subPer(r,nums,[],{});
    return(r);
};

var inputi = [1,2,3];
var r = permute(inputi);
console.log(r);
console.log('-----------the end!----------------');

