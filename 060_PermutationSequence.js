/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    //Runtime: 3848 ms, faster than 14.00% of JavaScript online submissions for Permutation Sequence.
    //Memory Usage: 196.8 MB, less than 11.11% of JavaScript online submissions for Permutation Sequence.
    var getSubPermutation=function(n,k,r,used,tmp){
        if(r.length===k){
            return;
        };
        if(tmp.length===n){
            r.push(tmp.slice());
            return;
        };
        for(var i=1;i<n+1;i++){
            if (used[i]===undefined){
                used[i]=1;
                tmp.push(i.toString());
                getSubPermutation(n,k,r,used,tmp);
                tmp.pop();
                used[i]= undefined;
            };  
        };
    }
    var r=[];
    var used={};
    var tmp=[];
    getSubPermutation(n,k,r,used,tmp);
    return(r.pop().join(""));
};

var getPermutation2 = function(n, k) {
    //Runtime: 60 ms, faster than 100.00% of JavaScript online submissions for Permutation Sequence.
    //Memory Usage: 34.2 MB, less than 44.44% of JavaScript online submissions for Permutation Sequence.
    let res='';//the return string
    let arr='123456789'.split('');

    let f=[];//saved the n! value
    f[0]=1;
    for(let i=1;i<n;i++){
        f[i]=f[i-1]*i;
    }

    k--;
    for(let i=n;i>=1;i--){
        //get right number in order. 
        let j=parseInt(k/f[i-1]);
        k%=f[i-1];
        res+=arr[j];
        //remove the arr[j] and return the new arr
        //make sure no duplicated num and in the correct order
        arr.splice(j,1);
    }
    return res;
};
var inputi = 3,k2=3;
console.log(getPermutation2(inputi,k2));
console.log('-----------the end!----------------');

