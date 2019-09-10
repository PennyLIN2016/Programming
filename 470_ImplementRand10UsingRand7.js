/**
 * The rand7() API is already defined for you.
 * var rand7 = function() {}
 * @return {number} a random integer in the range 1 to 7
 */
//Runtime: 124 ms, faster than 26.53% of JavaScript online submissions for Implement Rand10() Using Rand7().
//Memory Usage: 40.1 MB, less than 100.00% of JavaScript online submissions for Implement Rand10() Using Rand7().
var rand10 = function() {
    var rand49=function(){
        return 7*(rand7()-1)+rand7()-1;
    };
    var rand40=function(){
        var num=rand49();
        while(num>=40){num=rand49();};
        return num;
    };
    return rand40()%10 +1;
};
//var inlist="c";
//console.log(inlist);
console.log(rand10());
console.log('-----------the end!----------------');