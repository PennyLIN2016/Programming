/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    //Runtime: 56 ms, faster than 100.00% of JavaScript online submissions for Unique Paths.
    //Memory Usage: 33.9 MB, less than 58.21% of JavaScript online submissions for Unique Paths.
    var r = new Array(n);
    r.fill(1);
    for (var i = 1;i<m;i++){
        for(var j = 1;j<n;j++){
            r[j]+=r[j-1];
        };
    };
    return(r[n-1]);
};

var inputi = 4,k2=5;
console.log(uniquePaths(inputi,k2));
console.log('-----------the end!----------------');

