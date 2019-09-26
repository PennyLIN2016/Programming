/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
//Runtime: 64 ms, faster than 65.60% of JavaScript online submissions for Teemo Attacking.
//Memory Usage: 38.3 MB, less than 100.00% of JavaScript online submissions for Teemo Attacking.
var findPoisonedDuration = function(timeSeries, duration) {
    var res=0;
    var pre=-duration;
    for(var i=0;i<timeSeries.length;i++){
        if (timeSeries[i]-pre>=duration){
            res+=duration;
        }else{
            res+=timeSeries[i]-pre;
        };
        pre=timeSeries[i]
    };
    return res;
};
var S = [1,4];
var a= 2


//console.log(inlist);

console.log(findPoisonedDuration(S,a));
console.log('-----------the end!----------------');