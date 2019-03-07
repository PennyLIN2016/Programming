/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var list = [
        [1,1000,'M'],
        [0,900,'CM'],
        [0,500,'D'],
        [0,400,'CD'],
        [1,100,'C'],
        [0,90,'XC'],
        [0,50,'L'],
        [0,40,'XL'],
        [1,10,'X'],
        [0,9,'IX'],
        [0,5,'V'],
        [0,4,'IV'],
        [1,1,'I']
    ];
    var i = 0;
    var Roman_str='';
    var tmp = 0;
    while (i<list.length){
        if(list[i][0]===1){
            tmp = Math.floor(num/list[i][1]);
            for (var j=0;j<tmp;j++){
                Roman_str+= list[i][2];
            };
            num = num%list[i][1];
        }else{
            if (num-list[i][1] >=0){
                Roman_str+= list[i][2];
                num -= list[i][1]
            };
        };
        if (num===0){
            return(Roman_str);
        };
        i++;
    }; 
    
};



var input_example = 9;

console.log(intToRoman(input_example));