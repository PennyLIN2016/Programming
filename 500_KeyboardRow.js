/**
 * @param {string[]} words
 * @return {string[]}
 */
//Runtime: 48 ms, faster than 88.24% of JavaScript online submissions for Keyboard Row.
//Memory Usage: 34.1 MB, less than 12.50% of JavaScript online submissions for Keyboard Row.
var findWords = function(words) {
    var l1= new Set(['q','w','e','r','t','y','u','i','o','p']);
    var l2= new Set(['a','s','d','f','g','h','j','k','l']);
    var l3= new Set(['z','x','c','v','b','n','m']);
    var res=[];
    for(var i=0;i<words.length;i++){
        if(words[i].length===0){
            continue;
        };
        var cur=words[i].toLowerCase();
        var l;
        if(l1.has(cur[0])){l=l1;}
        else if (l2.has(cur[0])){
            l=l2;
        }else if (l3.has(cur[0])){
            l=l3;
        }else{
            continue;
        };
        res.push(words[i]);
        for(var j = 1;j<cur.length;j++){
            if(!l.has(cur[j])){
                res.pop();
                break;
            };
        };
    };
    return res;
    
};
var S = ["Hello", "Alaska", "Dad", "Peace"];

console.log(findWords(S));
console.log('-----------the end!----------------');