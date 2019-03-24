/**
 * @param {number} n:1<= n<= 30
 * @return {string}
 */
var countAndSay = function(n) {
    var PreCountAndSay= function(l){
        if(l===1){
            return('1');
        };
        var tmp_str = PreCountAndSay(l-1),
            re_str = '',
            i = 0,
            tmp_sign,
            tmp_l = 0;

        while(i<tmp_str.length){
            if (tmp_l===0){
                tmp_sign = tmp_str[i];
                tmp_l =1;  
                continue;
            }else{
                while(i+tmp_l < tmp_str.length && ltmp_str[i+tmp_l]===tmp_sgin){
                    tmp_l++;
                };
                re_str += (tmp_l).toString() +tmp_str.toString();
                tmp_l = 0;
                };
            };

            i += tmp_l-1;
        };
        return(re_str);
    };

    return(PreCountAndSay(n));  
};

var n=4;
console.log(countAndSay(n));
console.log('the end!');