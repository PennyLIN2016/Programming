/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert1 = function(nums, target) {//faster than 70.97%
    var i = 0;
    while(i<nums.length){
        if(nums[i]>=target){
            return(i);
        }else{
            i++;
        };
    };
    return(i);
};
var searchInsert = function(nums, target) {// faster than 90.21%
    var l = 0;
        r = nums.length-1;
        mid = 0; mid = Math.floor((l+r)/2);

    while(l<=r){
        mid = Math.floor((l+r)/2);
        if(nums[mid]==target){
            return(mid);
        }else if(nums[mid]<target){
            l = mid+1;
        }else{
            r= mid-1;
        };
    };
    return((Math.ceil((l+r)/2)));
};
var in_list = [1,3,5,9];
var target = 5;

console.log(searchInsert(in_list,target));
console.log('-----------the end!----------------');