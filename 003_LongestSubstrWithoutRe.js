/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    if (s.length === 0){
        return 0;
    }
    var d = {};
    var max_len= 0;
    var start = 0;
    var i = 0;
    for (i=0;i<s.length;i++){
        if (d[s[i]]!==undefined){
            start = Math.max(start,d[s[i]]+1);
        };
        d[s[i]]= i;
        max_len = Math.max(max_len,i-start+1);

    };
    return max_len;
};


var str_example = 'pwwkew';
//var r = lengthOfLongestSubstring(str_example);

console.log(lengthOfLongestSubstring(str_example));