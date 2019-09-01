/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
//Runtime: 84 ms, faster than 80.71% of JavaScript online submissions for Assign Cookies.
//Memory Usage: 37.7 MB, less than 100.00% of JavaScript online submissions for Assign Cookies.
//time:o(nlgn+nlgn+n)=o(nlgn)  space:o(1)
var findContentChildren = function(g, s) {
    var p2=0;
    var res=0;
    g.sort(function(a,b){return a-b});
    s.sort(function(a,b){return a-b});
    for(var i=0;i<g.length && p2<=s.length;i++)
    {
        while(g[i]>s[p2] && p2<s.length)p2+=1;
        if(g[i]<=s[p2])
        {
            res+=1;
            p2+=1;
        };
    };
    return res;  
};

var g=[10,9,8,7],c= [5,6,7,1];
//console.log(in_list);
console.log(findContentChildren(g,c));
console.log('-----------the end!----------------');