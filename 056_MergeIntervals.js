/**
* @param {number[][]} intervals
* @return {number[][]}
*/
var merge = function(intervals) {
    //Runtime: 80 ms, faster than 96.09% of JavaScript online submissions for Merge Intervals.
    //Memory Usage: 36.4 MB, less than 100.00% of JavaScript online submissions for Merge Intervals.
    if (intervals.length<=1){
        return(intervals);
    };
    intervals= intervals.sort((a,b)=>a[0]-b[0]);
    //console.log(intervals);
    var r=[];
    r.push(intervals[0]);
    for(var i=1;i<intervals.length;i++){
        tmp= r.pop();
        if(tmp[1]>=intervals[i][0]){
            tmp[1]=Math.max(tmp[1],intervals[i][1]);
            r.push(tmp);
            continue;
        };
        r.push(tmp);
        r.push(intervals[i]);
    };
    return(r);
};
var inputi = [[1,4],[4,5]];
console.log(merge(inputi));
console.log('-----------the end!----------------');

