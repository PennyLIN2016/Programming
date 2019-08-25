/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    //Runtime: 64 ms, faster than 76.90% of JavaScript online submissions for String Compression.
    //Memory Usage: 37.6 MB, less than 100.00% of JavaScript online submissions for String Compression.
    if(chars===[]){return 0};
    var newI=1,pre=chars[0],pre_count=1;
    for(i=1;i<chars.length;i++){
        if(pre!=chars[i]){
            pre=chars[i]
            if (pre_count>1){
                var tmp= pre_count.toString();
                for(var j=0;j<tmp.length;j++){
                    chars[newI++]=tmp[j]
                };
            };
            chars[newI]=chars[i]
            newI++
            pre_count=1

        }else{
            pre_count++
        }
    };
    if(pre_count>1){
        var tmp= pre_count.toString();
        for(var j=0;j<tmp.length;j++){
                chars[newI++]=tmp[j]
        };
    };

    while(chars.length>newI){chars.pop()};
    return newI;
};

var in_list = ["a","a","b","b","c","c","c"];
console.log(in_list);
console.log(compress(in_list));
console.log('-----------the end!----------------');