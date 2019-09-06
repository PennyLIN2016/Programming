/**
 * @param {string} s
 * @return {boolean}
 */
//Runtime: 60 ms, faster than 92.39% of JavaScript online submissions for Repeated Substring Pattern.
//Memory Usage: 36.2 MB, less than 100.00% of JavaScript online submissions for Repeated Substring Pattern.
var repeatedSubstringPattern = function(s) {
    var doubleS= (s+s).substring(1,s.length*2-1);
    return doubleS.includes(s);
};
var inlist="abcabcabcabc";
console.log(inlist);
console.log(repeatedSubstringPattern(inlist));
console.log('-----------the end!----------------');