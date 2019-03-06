/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if(x==0){
        return(0)
    };
    var i= 0,j=1;
    var s_n = '';
    var curr_n = 0
    if (x<0){
        s_n+='-';
        x= Math.abs(x);
        
    };   
    while(x>0){
        i= x%10;
        if(i!==0||s_n!='-'||s_n!==''){
            s_n+=i.toString();
        };
        curr_n = Math.abs(parseInt(s_n));
        if (curr_n>0x7FFFFFFF){
            return 0
        };
        x= Math.floor(x/10);
    };
    return(parseInt(s_n));
};

var number_example = -123;
console.log(reverse(number_example));