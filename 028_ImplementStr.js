/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle){
    if (needle===''){
        return(0);
    };
    var i= 0,j= 0;
    for(i=0;i<=haystack.length-needle.length;i++){
        for(j=0;j<needle.length;j++){
            if(haystack[i+j]!=needle[j]){
                j= needle.length +1;
                break;
            };
        };
        if(j===needle.length){
            return(i)
        };
    };
    return(-1); 
};

var str_example = 'hello';
var sub = 'll';

console.log(strStr(str_example,sub));
console.log('-----------the end!----------------');