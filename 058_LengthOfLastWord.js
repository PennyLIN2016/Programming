/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    //Runtime: 56 ms, faster than 100.00% of JavaScript online submissions for Length of Last Word.
    //Memory Usage: 33.9 MB, less than 20.66% of JavaScript online submissions for Length of Last Word.
    s = s.trim();
    if(s.length===0){
        return(0);
    };
    var s_l= s.split(' ');
    return(s_l.pop().length);
};
var inputi = "H ";
console.log(lengthOfLastWord(inputi));
console.log('-----------the end!----------------');

