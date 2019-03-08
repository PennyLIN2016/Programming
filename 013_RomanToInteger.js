/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    if (s.length===0){
        return(0);
    };
    
    var dict_map = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,
                     'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1};
    var i=0, sum_num = 0;
    while (i<s.length){
        if (i+1<s.length){
            if (dict_map[s.substring(i,i+2)]!==undefined){
                sum_num += dict_map[s.substring(i,i+2)];
                i= i+2;
                continue;
            };
        };
        sum_num += dict_map[s[i]];
        i++;
    };
    return(sum_num)
};
var in_example = "IV";
console.log(romanToInt(in_example));