/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length<=1){
        return(nums.length);
    };
    var i= 0, end= 0;
    for(i=1;i<nums.length;i++){
        if(nums[i]!==nums[end]){
            end++;
            nums[end]=nums[i]
        };
    };
    return(end+1);  
};

var string_example =[1,1,2];
console.log(removeDuplicates(string_example));
console.log(string_example);
console.log('-----------the end!----------------');