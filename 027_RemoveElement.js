/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    if(nums.length===0){
        return(0);
    };
    var i = 0,end=0;
    for(i=0;i<nums.length;i++){
        if(nums[i]!==val){
            nums[end]=nums[i];
            end++;
        };

    };
    return(end);
};

var string_example =[0,1,2,2,3,0,4,2];
var value = 2;
console.log(removeElement(string_example,value));
console.log(string_example);
console.log('-----------the end!----------------');