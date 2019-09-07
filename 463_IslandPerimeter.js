/**
 * @param {number[][]} grid
 * @return {number}
 */
//Runtime: 168 ms, faster than 91.73% of JavaScript online submissions for Island Perimeter.
//Memory Usage: 43.6 MB, less than 100.00% of JavaScript online submissions for Island Perimeter.
// time:o(h*m) space:o(1)
var islandPerimeter = function(grid) {
    var h= grid.length;
    if(h){var w=grid[0].length}else{var w=0};
    var res=0
    for(var i=0;i<h;i++)
    {
        for(var j=0;j<w;j++)
        {
            if(grid[i][j]){
                res+=4;
                if(i>0 && grid[i-1][j]) res-=2;
                if(j>0 && grid[i][j-1]) res-=2;
            };

        };
    };
    return res
    
};
var inlist=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]];
//console.log(inlist);
console.log(islandPerimeter(inlist));
console.log('-----------the end!----------------');