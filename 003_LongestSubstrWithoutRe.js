/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    if (s.length === 0){
        return 0;
    }
    var d = {};// save the existing chars in s. char:i i is the last pos in s. 
    var max_len= 0;// current max length
    var start = 0;// the start pos of the current compared sub string
    var i = 0;
    for (i=0;i<s.length;i++){
        if (d[s[i]]!==undefined){// found a repeated char
            // the new compared sub string starts from the next char of the repeated pos.
            start = Math.max(start,d[s[i]]+1);
        };
        // refresh the last pos of the char
        d[s[i]]= i;
        //compare currentsub string to the max  len.  
        max_len = Math.max(max_len,i-start+1);

    };
    return max_len;
};


var str_example = 'pwwkew';
//var r = lengthOfLongestSubstring(str_example);

console.log(lengthOfLongestSubstring(str_example));
