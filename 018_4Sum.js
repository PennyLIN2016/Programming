/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    if(nums.length<4){
        return([]);
    };
    var i= 0;
    var re_list = [];
    nums.sort(function(a,b){return(a-b)});
    console.log(nums);
    while(i<nums.length-3){
        if(i>0 && nums[i]===nums[i-1]){
            i++;
            continue;
        };
        var j = i+1;
        while(j<nums.length-2){
            if(j>i+1 && nums[j]===nums[j-1]){
                j++;
                continue;
            };
            var l=j+1, r=nums.length-1;
            while(l<r){
                var sum_cur = nums[i]+nums[j]+nums[l]+nums[r];
                if(sum_cur === target){
                    re_list.push([nums[i],nums[j],nums[l],nums[r]]);
                    l++;
                    if(l<r && nums[l]===nums[l-1]){
                        l++;
                    };
                    r--;
                    if(l<r &&nums[r]===nums[r+1]){
                        r--;
                    };
                }else if(sum_cur > target){
                    r--;
                }else{
                    l++;
                };
                console.log([i,j,l,r]);
            }
            j++;
        };
        i++;
    };
    return(re_list);
};

var string_example =[4,-9,-2,-2,-7,9,9,5,10,-10,4,5,2,-4,-2,4,-9,5];
var target = -13;
console.log(fourSum(string_example,target));
