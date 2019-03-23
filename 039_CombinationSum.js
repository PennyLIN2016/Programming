/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum1 = function(candidates, target) {//success in local pc ,but there are type error in leecode, should be tmp_can`s problem 
    var preCom = function(candidates,tmp_can,pos,cur_stack,target){
        if(target === 0){
            cur_stack.push(tmp_can +[]);// the [] make sure the elemts in cur_stack will change when tmp_can changes.
            return;
        };
        var i;
        for(i=pos;i<candidates.length;i++){
            if(candidates[i]<=target){
                tmp_can.push(candidates[i]);
                preCom(candidates,tmp_can,i,cur_stack,target-candidates[i]);
                tmp_can.pop();
            }else{
                break;
            };
        };
        return;
    };
    var r = [],
        tmp_can = [];

    candidates.sort(function(a,b){return(a-b)});
    preCom(candidates,tmp_can,0,r,target);
    return (r);
};


var combinationSum = function(candidates, target) {//faster than 75%
    var r = [],tmp = [];
    var preCom = function(tmp_can,pos,target){
        var i;
        for(i=pos;i<candidates.length;i++){
            if(candidates[i]===target){
                r.push(tmp_can.concat(candidates[i]));
                
            }else if(candidates[i]>target){
                break;
            }else{
                preCom(tmp_can.concat([candidates[i]]),i,target-candidates[i]);
            };
        };
        return;
    };
    candidates.sort(function(a,b){return(a-b)});
    preCom(tmp,0,target);
    return (r);
};


var in_list = [2,3,6,7];
var target = 7;

console.log(combinationSum(in_list,target));
console.log('-----------the end!----------------');