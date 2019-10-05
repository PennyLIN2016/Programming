/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
//Runtime: 56 ms, faster than 90.22% of JavaScript online submissions for Next Greater Element I.
//Memory Usage: 36.5 MB, less than 100.00% of JavaScript online submissions for Next Greater Element I.
var nextGreaterElement = function(nums1, nums2) {
    var pos={};
    var res=[];
    for(var i=0;i<nums2.length;i++){
        pos[nums2[i].toString()]=i;
    };
    for(var j =0 ;j<nums1.length;j++){
        var cur=pos[nums1[j].toString()];
        res.push(-1);
        for(var p = cur+1;p<nums2.length;p++){
            if(nums2[p]>nums1[j]){
                res[res.length-1]=nums2[p];
                break;
            };
        };
    };
    return res
};
var S = [4,1,2], b = [1,3,4,2];

console.log(nextGreaterElement(S,b));
console.log('-----------the end!----------------');