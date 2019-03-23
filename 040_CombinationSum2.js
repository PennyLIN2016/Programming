/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {//faster than 93%
    var r = [],tmp=[];
    var preCom = function(tmp_can,pos,target){
        if (target ===0){
            r.push(tmp_can)
            return;
        };
        var i;
        for(i=pos;i<candidates.length && target>= candidates[i];i++){
            if(i>pos && candidates[i]===candidates[i-1]){// meake sure no dubplicate elements.
                continue;
            }; 
            preCom(tmp_can.concat([candidates[i]]),i+1,target-candidates[i]);
        };
    };
    candidates.sort((a,b)=>a-b);
    preCom(tmp,0,target);
    return (r);
};


var in_list = [10,1,2,7,6,1,5];
var target = 8;

console.log(combinationSum2(in_list,target));
console.log('-----------the end!----------------');