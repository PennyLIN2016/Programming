/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
//Runtime: 52 ms, faster than 80.10% of JavaScript online submissions for Hamming Distance.
//Memory Usage: 34 MB, less than 37.50% of JavaScript online submissions for Hamming Distance.
var hammingDistance = function(x, y) {
    var tmp=x^y;
    var res=0;
    for(var i=0;i<32;i++){
        if(tmp&1){res++};
        tmp>>>=1;
    };
    return res  
};
var inlist=1;
var y=6
//console.log(inlist);
console.log(hammingDistance(inlist,y));
console.log('-----------the end!----------------');