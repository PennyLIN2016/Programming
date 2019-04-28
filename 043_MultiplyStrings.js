/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */

var multiply = function(num1, num2) {
    //Runtime: 76 ms, faster than 84.80% of JavaScript online submissions for Multiply Strings.
    //Memory Usage: 35.8 MB, less than 75.00% of JavaScript online submissions for Multiply Strings
    if (num1.length===0 || num2.length===0){
        return('0');
    };
    var r = Array(num1.length+num2.length).fill(0);
    for(i = num1.length-1;i>=0;i--){
        for (j= num2.length-1;j>=0;j--){
            r[i+j+1]+= parseInt(num1[i])* parseInt(num2[j]);
            r[i+j] += Math.floor(r[i+j+1]/10);
            r[i+j+1] = r[i+j+1]%10;
        };
    };
    pos = 0
    while(pos<r.length-1){
        if (r[pos]!==0){
            break;
        };
        pos++;
    };
    return(r.slice(pos,r.length).join(''));
};

var num1 = '4568',num2 = '10356';

console.log(multiply(num1,num2));
console.log('-----------the end!----------------');