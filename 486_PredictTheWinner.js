/**
* @param {number[]} nums
* @return {boolean}
*/
// my local is ok , but the leecode raised wrong answer, in this case, the j/end can be 3???
var sD= {},fD={};
var PredictTheWinner = function(nums) {
    var total= nums.reduce((a,b)=>a+b,0);
    var one=f(nums,0,nums.length-1)
    console.log(2*one>=total);
    console.log(sD);
    console.log(fD);
    
    return 2*one>=total;
   
};
var f=function(l,start,end){

    if (start==end){
        return l[start];
    };
    
    // fD[[start,end] is ok in my local , but error in leecode
    if(fD[[start,end]]===undefined){
        fD[[start,end]]= Math.max(l[start]+s(l,start+1,end),l[end]+s(l,start,end-1));
    };
    return fD[[start,end]];

};
var s=function(l,i,j){
    if (i==j){
        return 0;
    };
    if(sD[[i,j]]===undefined){
        sD[[i,j]]= Math.min(f(l,i+1,j),f(l,i,j-1));
    };
    return sD[[i,j]];
};

var S = [1,3,1];


//console.log(inlist);
console.log(PredictTheWinner(S));
console.log('-----------the end!----------------');