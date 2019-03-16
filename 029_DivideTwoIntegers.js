/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide1 = function(dividend, divisor) {//correct but too slow.
    var flag = 0;
    if((dividend<0 && divisor>0)||(dividend>0 && divisor<0)){
        flag= -1
    };
    var a = Math.abs(dividend),b = Math.abs(divisor);
    if(b==1){
        if(flag==-1){
            return(Math.max(-1*a, -2147483648));
        }else{
            return(Math.min(a,0x7fffffff))
        }; 
    };
    var t= 1,sub_tmp=b,r=0;
    while(a>=b){
        while((sub_tmp<<1)<=a){
            t<<=1;
            sub_tmp<<=1;
        };
        r+= t;
        t=1
        a-=sub_tmp;
        sub_tmp= b;
    };

    if(flag==-1){
        return(Math.max(-1*r, -2147483648));
    }else{
        return(Math.min(r,0x7fffffff))
    }; 
};

var divide = function(dividend, divisor) {//faster than 88.32%
    var MAX_INT = Math.pow(2, 31) - 1,
        MIN_INT = -Math.pow(2, 31),
        result = 0,
        newDividend = Math.abs(dividend),
        newDivisor = Math.abs(divisor),
        flag;
    if (newDividend < newDivisor) {
        return 0;
    }
    if (dividend >= 0 && divisor > 0 || dividend <= 0 && divisor < 0) {
        flag = 1;
    } else {
        flag = -1;
    }
    while (newDividend >= newDivisor) {
        var temp = newDivisor,
            i = 0;
        while (newDividend >= temp << 1) {
            if ((temp << 1) <= 0) {
                break;
            }
            temp = temp << 1;
            i++;
            if (flag > 0 && i > 29) {
                return MAX_INT;
            }
            if (flag < 0 && i > 30) {
                return MIN_INT;
            }
        }
        newDividend -= temp;
        result += Math.pow(2, i);
    }
    if (flag > 0) {
        return result;
    } else {
        return -result;
    }
};
var dividend = 67798799768;
var divisor = -3;

console.log(divide(dividend,divisor));
console.log('-----------the end!----------------');