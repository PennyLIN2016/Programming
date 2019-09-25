/**
 * @param {number} area
 * @return {number[]}
 */
//Runtime: 56 ms, faster than 75.17% of JavaScript online submissions for Construct the Rectangle.
//Memory Usage: 34.5 MB, less than 100.00% of JavaScript online submissions for Construct the Rectangle.
var constructRectangle = function(area) {
    for(var i = Math.floor(Math.sqrt(area));i>0;i--){
        if(area%i===0) return([area/i,i]);
    };
};
var S = 4;


//console.log(inlist);

console.log(constructRectangle(S));
console.log('-----------the end!----------------');