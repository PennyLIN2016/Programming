/**
 * @param {number[][]} points
 * @return {number}
 */
//Runtime: 180 ms, faster than 96.15% of JavaScript online submissions for Number of Boomerangs.
//Memory Usage: 41.2 MB, less than 100.00% of JavaScript online submissions for Number of Boomerangs.
var numberOfBoomerangs = function(points) {
    var res=0;
    for(var i=0;i<points.length;i++){
        var map = new Map();
        for (var j=0;j<points.length;j++){
            if(i===j){ continue};
            var d=TwoDistance(points[i],points[j]);
            // get the current count of d in the map
            // get the int of map.get(). ~~ not bit operartion, fast inmplementation of Math.floor
            var count=~~map.get(d);
            // set the count of d in map
            map.set(d,count+1);
            res+=count;
        }

    };
    return res*2

    
};
function TwoDistance(p1,p2){
    return((p1[1]-p2[1])*(p1[1]-p2[1])+(p1[0]-p2[0])*(p1[0]-p2[0]))
};

var in_list =[[0,0],[1,0],[2,0]];
console.log(in_list);
console.log(numberOfBoomerangs(in_list));
console.log('-----------the end!----------------');