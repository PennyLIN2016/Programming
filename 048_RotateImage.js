/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    //Runtime: 56 ms, faster than 100.00% of JavaScript online submissions for Rotate Image.
    //Memory Usage: 33.8 MB, less than 46.15% of JavaScript online submissions for Rotate Image.
    if (matrix.length <2){
        return(matrix);
    };
    var n = matrix.length
    var i,j,tmp;
    for (i=0;i<Math.ceil(n/2);i++){
        for(j=0;j<Math.floor(n/2);j++){
            tmp=matrix[i][j];
            matrix[i][j]=matrix[n-1-j][i];
            matrix[n-1-j][i]=matrix[n-1-i][n-1-j];
            matrix[n-1-i][n-1-j]=matrix[j][n-1-i];
            matrix[j][n-1-i]=tmp;
        };
    };
    return(matrix)
};


    

var m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ];
console.log(m);
console.log(rotate(m));
console.log('-------the end!--------');