/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    if(n<=0){
        return(n);
    }
    
    var r_l = [];
    r_l.push(1);
    var c_n = 1;
    var i_2=0,i_3=0,i_5=0
    while(c_n<n){
        var min_n = Math.min(2*r_l[i_2],3*r_l[i_3],5*r_l[i_5]);
        if (min_n==2*r_l[i_2]){i_2++};
        if (min_n==3*r_l[i_3]){i_3++};
        if (min_n==5*r_l[i_5]){i_5++};
        c_n++;
        r_l.push(min_n);
    };
    return(r_l.pop()) 
};
var target = 13;
console.log(nthUglyNumber(target));
console.log('the end!');