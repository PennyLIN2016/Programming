/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    var len = nums.length;
    if (len<3){
        return(null)
    };

    nums.sort(function(a,b){return(a-b)});
    var mix_gap = Infinity;
    sum_cur = null
    var f= 0;
    while (f<len-2){
        var l= f+1,r=len-1;
        if(f>0 && nums[f]==nums[f-1]){
            f++;
            continue;
        };
        while(l<r){        
            tmp_sum = nums[f]+nums[l]+nums[r];
            if (tmp_sum=== target){
                return(target);
            } else if (tmp_sum > target){
                if(tmp_sum-target < mix_gap){
                    mix_gap = tmp_sum-target;
                    sum_cur = tmp_sum;
                };
                r--
                while(l<r && nums[r]===nums[r+1]){
                    r--
                };   
            }else{
                if(target - tmp_sum < mix_gap){
                    mix_gap = target - tmp_sum;
                    sum_cur = tmp_sum;
                };
                l++
                while(l<r && nums[l]===nums[l-1]){
                    l++;
                }; 
            };
        };
        f++;
    };
    return(sum_cur)
};

var string_example =[-1, 2, 1, -4];
var target = 1;
console.log(threeSumClosest(string_example,target));