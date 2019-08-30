/**
 * @param {number[][]} points
 * @return {number}
 */
//Runtime: 108 ms, faster than 48.91% of JavaScript online submissions for Minimum Number of Arrows to Burst Balloons.
//Memory Usage: 42.6 MB, less than 100.00% of JavaScript online submissions for Minimum Number of Arrows to Burst Balloons.
var findMinArrowShots = function(points) {
    if(!points||points.length==0){return 0};
    points.sort(function(x1,x2){return x1[1]-x2[1]});
    var res=1,right=points[0][1];
    for(var i=1;i<points.length;i++){
        if (points[i][0]>right){
            res+=1;
            right=points[i][1];
        };
    };
    return res
};
var in_list =[[10,16], [2,8], [1,6], [7,12]];
console.log(in_list);
console.log(findMinArrowShots(in_list));
console.log('-----------the end!----------------');