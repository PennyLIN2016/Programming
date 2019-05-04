/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    //Runtime: 56 ms, faster than 99.72% of JavaScript online submissions for Spiral Matrix.
    //Memory Usage: 33.8 MB, less than 34.34% of JavaScript online submissions for Spiral Matrix.

    if (matrix.length===0||matrix[0]===0){
        return(matrix);
    };

    var r = [];
    var i = 0,j= 0,k;
    var h= matrix.length,w=matrix[0].length;
    while(h>0 && w>0){
        for(k=j;k<w+j;k++){
            r.push(matrix[i][k]);
        };
        h-=1;
        i+=1;
        j+=w-1;
        if (h===0){break;};
        for(k=i;k<i+h;k++){
            r.push(matrix[k][j]);
        };
        w-=1;
        i+=h-1;
        j=j-1;
        if (w===0){break;};
        for(k=j;k>j-w;k--){
            r.push(matrix[i][k]);
        };
        h-=1;
        j-=w-1;
        i-=1;
        if (h===0){break;};
        for(k=i;k>i-h;k--){
            r.push(matrix[k][j]);
        };
        w-=1;
        i-=h-1;
        j+=1;      
    };
    return(r);
};

var inputi = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
  ];
console.log(spiralOrder(inputi));
console.log('-----------the end!----------------');

