/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    
    if(s.length <= numRows || numRows<= 1){
        return(s)
    };

    var size = 2*numRows-2;
    var r_s = [];
    var i =0;l= s.length;

    while(i<numRows){
        var p =i, k= -i;
        while(p<l ||k<l){
            if (0<=k<l && p!=k && i!=numRows-1){
                r_s.push(s[k]);
            };
            if(p<l){
                r_s.push(s[p]);
            };
            p+=size;
            k+=size;
        };
        i++;
    };
    return(r_s.join(''))
};

var s= "PAYPALISHIRING", Rows_num=3;

console.log(convert(s,Rows_num));
