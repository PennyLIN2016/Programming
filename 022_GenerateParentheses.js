/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var re_generate= function(l,r,stack_str,str1){
        if (l==0 && r===0){
            stack_str.push(str1);
            return
        };
        var str_in = '';
        if (l>0){
            str_in = str1+'(';
            l--;
            if(r>=l){re_generate(l,r,stack_str,str_in);}
            l++;
        };
        if (r>0){
            str_in = str1+')';
            r--;
            if(r>=l){re_generate(l,r,stack_str,str_in);}
            r++;
        };
    };
    var left_n = n, right_n =n;
    var re_str=[];
    var cur_str= '';
    re_generate(left_n,right_n,re_str,cur_str);
    return(re_str);
};

var n=4;
console.log(generateParenthesis(n));
console.log('the end!');