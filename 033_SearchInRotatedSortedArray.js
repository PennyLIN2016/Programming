/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (nums.length==0){
        return(-1);
    };
    var l = 0, r = nums.length-1;
    var mid;
    while(l<=r){
        mid = Math.floor((l+r)/2);
        if(nums[mid]==target){
            return(mid);
        }else if (nums[mid]>=nums[l]){
            if(nums[l]<= target && target <= nums[mid]){
                r = mid -1;
            }else{
                l= mid + 1;
            };
        }else{
            if(nums[r] >= target && target >= nums[mid]){
                l = mid + 1;
            }else{
                r = mid - 1;
            };
        };
    };
    return(-1);  
};

var string_example =[3,1];
var value = 1;
console.log(search(string_example,value));
console.log('-----------the end!----------------');