
var dict ={
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z'],
};
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var getsubstr = function(num_str,letter_str,out_re){
        if (num_str.length===0){
            out_re.push(letter_str);
            return;
        };

        var letter_list = dict[num_str[0]];
        var i =0;
        while(i<letter_list.length){
            var letter_current = letter_str+ letter_list[i];
            var num_left = num_str.substring(1,num_str.length);
            getsubstr(num_left,letter_current,out_re);
            i++;
        };
    };
    if (digits.length===0){
        return([]);
    };
    var out_re =[];
    getsubstr(digits,'',out_re);
    return(out_re);
};

var string_example ='295';
console.log(letterCombinations(string_example));