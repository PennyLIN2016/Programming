/**
 * @param {string} s
 * @return {string}
 */
var IsPalindromic = function(sub_s){
    //return True if the sub_s is palindromic, otherwise return False
    if (sub_s===''){
        return true;
    };
    var j = sub_s.length-1,i= 0;
    while (i<j){
        if (sub_s[i]!=sub_s[j]){
            return false;
        };
        j--;
        i++;
    };

};
var longestPalindrome = function(s) {
    var left = 0,right = 0,i = 0,s_len = s.length;
    while(i<s_len-1){
        if(2*(s_len-i)+1 < right-left+1){
            break;
        };
        var l = i, r = i;
        while(l>=0 && r<s_len &&s[l]===s[r]){
            l--;
            r++;
        };
        if (r-l-2 > right-left){
            left=l+1;
            right=r-1;
        };
        l=i;
        r=i+1;
        while(l>=0 && r<s_len &&s[l]===s[r]){
            l--;
            r++;
        };
        if (r-l-2 > right-left){
            left = l+1;
            right = r-1;
        };
        i++;
    };

    return s.substring(left,right+1)
    
};

var str_example = 'babad';

var re_str = longestPalindrome(str_example);

console.log('result : '+ re_str);