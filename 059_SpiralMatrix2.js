/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    //Runtime: 56 ms, faster than 100.00% of JavaScript online submissions for Spiral Matrix II.
    //Memory Usage: 33.9 MB, less than 50.00% of JavaScript online submissions for Spiral Matrix II.
    if (n<=0){
        return([]);
    };
    var r = new Array(n);
    for(var d=0;d<n;d++){
        r[d] = new Array(n);
    };
    var h=n,w=n,i=0,j=0,val=1;
    var k;
    while(val<=n*n){
        //->
        for(k=j;k<j+w;k++){
            r[i][k]=val;
            val++;
        };
        h-=1;
        j+=w-1;
        i+=1;
        if (val===n*n+1){break;};
        //down
        for(k=i;k<i+h;k++){
            r[k][j]=val;
            val++;
        };
        w-=1;
        i+=h-1;
        j-=1;
        if (val===n*n+1){break;};
        //<-
        for(k=j;k>j-w;k--){
            r[i][k]=val;
            val++;
        };
        h-=1;
        j-=w-1;
        i-=1;
        if (val===n*n+1){break;};
        //up
        for(k=i;k>i-h;k--){
            r[k][j]=val;
            val++;
        };
        w-=1;
        i-=h-1;
        j+=1;               
    };
    return(r);
};

var inputi = 7;
console.log(generateMatrix(inputi));
console.log('-----------the end!----------------');

