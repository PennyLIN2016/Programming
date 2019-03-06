/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var str_n = x.toString();
    var n = Math.floor(str_n.length/2);
    var i = 0;
    while (i<n){
        if (str_n[i]!=str_n[str_n.length-1-i]){
            return(false)
        };
        i++;
    };
    return(true)
};


var in_example = -121;

console.log(isPalindrome(in_example));