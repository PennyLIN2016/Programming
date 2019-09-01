/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */
//Runtime: 324 ms, faster than 50.68% of JavaScript online submissions for 4Sum II.
//Memory Usage: 78.5 MB, less than 50.00% of JavaScript online submissions for 4Sum II.
//time : o(n**2) space:o(n**2)
var fourSumCount = function(A, B, C, D) {
    var res=0;
    var countMap={};
    var l=A.length;
    for(var i=0;i<l;i++)
    {
        for(var j=0;j<l;j++)
        {
            var tmp=A[i]+B[j];
            if(countMap[tmp]===undefined)countMap[tmp]=1;
            else countMap[tmp]++;
        }
    };
    for(var i=0;i<l;i++)
    {
        for(var j=0;j<l;j++)
        {
            var tmp=C[i]+D[j];
            if(countMap[-tmp]!==undefined)res+=countMap[-tmp];
        }
    };
    return res
    
    
};

var A = [ 1, 2],B = [-2,-1],C = [-1, 2],D = [ 0, 2];

//console.log(in_list);
console.log(fourSumCount(A,B,C,D));
console.log('-----------the end!----------------');