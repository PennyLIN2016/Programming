/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    var str_con= str.trim();
    var i = -1;
    var flag= 0;
    var cur_num = 0;
    while (i<str_con.length-1){
        i++;
        if (str_con[i] == '-' && i == 0 ){
           flag = 1;
           continue;
        }else if(str_con[i] == '+' && i == 0){
            continue;
        }else if('0'.charCodeAt()<=str_con.charCodeAt(i) && str_con.charCodeAt(i)<='9'.charCodeAt()){
            cur_num = cur_num*10 + parseInt(str_con[i]);
            if (cur_num < 0x7FFFFFFF){
                continue;
            };
            if(flag===1 && cur_num == 0x7FFFFFFF) {
                return('-'+ (cur_num).toString());
            }else if (flag==1){
                return('-'+(0x7FFFFFFF+1).toString());
            }else{
                return((0x7FFFFFFF).toString());
            };
        }else if(cur_num!=0 ){
            if (flag==1){
                cur_num = -1*cur_num;
            };
            return(cur_num.toString());
        }else{
            return('0');
        };
    };
    // the last char is a number
    if (flag==1){
        cur_num = -1*cur_num;
    };
    return(cur_num.toString());
};


var string_example ="2147483648";

console.log(myAtoi(string_example));