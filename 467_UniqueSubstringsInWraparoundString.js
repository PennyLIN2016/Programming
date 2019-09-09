/**
 * @param {string} p
 * @return {number}
 */
// time out:19 / 81 test cases passed.
var findSubstringInWraproundString = function(p) {
    if(p.length<=1) return p.length;
    var posS=0,posE=1;
    var counted= new Set(p[posS]);
    while(posE<p.length){
        if(~counted.has(p[posE])) counted.add(p[posE]);
        if(p.charCodeAt(posE)===(p.charCodeAt(posE-1)+1)|(p[posE]==="a"&&p[posE-1]==="z")){
            for(var i =posS;i<posE;i++){
                if(~counted.has(p.substring(i,posE+1))) counted.add(p.substring(i,posE+1));
            };
        }else{
            posS=posE;
        };
        posE++;
    };
    return counted.size;
};
var inlist="c";
console.log(inlist);
console.log(findSubstringInWraproundString(inlist));
console.log('-----------the end!----------------');