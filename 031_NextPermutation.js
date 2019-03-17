/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    if(nums.length<=1){
        return;
    };
    var i= nums.length-1;
    // get the pos of the start the change
    while(i>0){
        if(nums[i-1]<nums[i]){
            break;
        };
        i--;
    };
    var j = nums.length-1,temp;
    // get the next great number in the pos 
    if(i>0){
        while(j>i-1){
            if(nums[j]>nums[i-1]){
                temp= nums[i-1];
                nums[i-1]= nums[j];
                nums[j]= temp;
                break;
            };
            j--;
        };
    };

    // after the pos, the left numbers should be in lowest possible order
    // at this point the nums,from i to end, should be greatest order. so just need to resever that.
    var r = nums.length-1, l= i;
    while(l<r){
        tmp = nums[l];
        nums[l] = nums[r];
        nums[r] = tmp;
        l++;
        r--;
    };   
};

var in_list = [1,3,2];
console.log(in_list);
nextPermutation(in_list);
console.log(in_list);
console.log('-----------the end!----------------');