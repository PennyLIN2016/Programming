/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var len= nums.length;
    if (len<3){
        return([]);
    };
    nums.sort(function(a, b){return a-b});
    if(nums[0]>0 || nums[nums.length-1]<0){
        return([]);
    };
    var i = 0;
    var re_list=[]
    while (i<len-1){
        if(nums[i]>0){
            break;
        };
        if(i>0 && nums[i]===nums[i-1]){
            i++;
            continue;
        };
        var target=0 - nums[i];
        var right= len-1,left= i+1;
        while(right>left){
            if(nums[right]+nums[left]=== target){
                re_list.push([nums[i],nums[left],nums[right]]);
                right--;
                while(right>left && nums[right]===nums[right+1]){
                    right--;
                };
                left++;
                while(right>left && nums[left]===nums[left-1]){
                    left++;
                };
            }else if(nums[right]+nums[left]>target){
                right--;
            }else{
                left++;
            };
        };
        i++;
    };
    return(re_list)
};
var string_example =[-1, 0, 1, 2, -1, -4];
console.log(threeSum(string_example));