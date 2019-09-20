/**
 * @param {string} S
 * @param {number} K
 * @return {string}
 */
var licenseKeyFormatting = function(S, K) {
    //Runtime: 60 ms, faster than 93.97% of JavaScript online submissions for License Key Formatting.
   //Memory Usage: 38.8 MB, less than 100.00% of JavaScript online submissions for License Key Formatting.
    var res='';
    console.log(S);
    // replace all occurance. if only replace the first occurance , S.replace('-','')
    var curS= (S.replace(/-/g,'')).toUpperCase()
    console.log(curS);
    l=curS.length;
    if(l%K){
        res=curS.substring(0,l%K)+'-';
    };
    console.log(res);
    for(var i=l%K;i<l;i+=K){
        res+=curS.substring(i,i+K)+'-';
    };
    if (res){res=res.substring(0,res.length-1)}
    return res
};
var S = "5F3Z-2e-9-w";
var  K = 3;

//console.log(inlist);
console.log(licenseKeyFormatting(S,K));
console.log('-----------the end!----------------');