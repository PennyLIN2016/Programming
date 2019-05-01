/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    //Runtime: 140 ms, faster than 65.77% of JavaScript online submissions for Group Anagrams.
    //Memory Usage: 46.7 MB, less than 29.09% of JavaScript online submissions for Group Anagrams.
    var re = {};
    var i = 0;
    var tmp = [];
    for (i=0;i<strs.length;i++){
        tmp = strs[i].split('').sort().join('');
        if(re[tmp]===undefined){
            re[tmp]= [];
        };
        re[tmp].push(strs[i]);
    };  
    return(Object.keys(re).map(function(key){return(re[key]);}));    
};

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams1 = function(strs) {
    //Runtime: 128 ms, faster than 89.24% of JavaScript online submissions for Group Anagrams.
    //Memory Usage: 44.3 MB, less than 96.36% of JavaScript online 
    var len=strs.length;
    var str=[];
    var res=new Map();
    for(var i=0;i<len;i++){
        //取键
        str=strs[i].split('').sort().join('');
        //存值
        if(!res.has(str)) 
            res.set(str,new Array())
        
        res.get(str).push(strs[i]);
    }
    return [...res.values()]
};

    

var str_in = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(str_in);
console.log(groupAnagrams(str_in));
console.log('-------the end!--------');