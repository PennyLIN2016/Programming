/**
* @param {number} num
* @return {number}
*/
//Runtime: 48 ms, faster than 94.07% of JavaScript online submissions for Number Complement.
//Memory Usage: 33.8 MB, less than 100.00% of JavaScript online submissions for Number Complement.
var findComplement = function(num) {
    var l= (num).toString(2).length;
    var mask=1;
    for(var i=0;i<l-1;i++){
        mask= (mask<<1) + 1
    };
   return (num ^ mask);
};
var inlist=5;
//console.log(inlist);
console.log(findComplement(inlist));
console.log('-----------the end!----------------');