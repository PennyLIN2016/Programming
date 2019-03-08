/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {//good solution 
    var commonprefix = function(str1,str2){
        var com_sub='';
        var l = 0
        if (str1.length<str2.length){
            l = str1.length;
            
        }else{
            l = str2.length;
        };
        while (l>=0){
            if (str1.substring(0,l+1)==str2.substring(0,l+1)){
                return(str1.substring(0,l+1));
            };
            l--;
        };
        return('');
    };
    switch(strs.length){
        case 0: return('');
        case 1: return(strs[0]);
        default:
            var long_pre = strs[0];
            var i = 1;
            while (i<strs.length){
                long_pre = commonprefix(long_pre,strs[i]);
                if (long_pre===''){
                    return('');
                };
                i++
            };
            return(long_pre)
    };    
};


var string_example =["aa","ab"];
console.log(longestCommonPrefix(string_example));