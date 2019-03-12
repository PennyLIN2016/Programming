/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {// faster
    var dict={
        "(":"0",
        "[":"0",
        "{":"0",
        ")":"(",
        "]":"[",
        "}":"{"
    };
    var i = 0;
    var tmp_s = [];
    for(i=0;i<s.length;i++){
        var tmp_char = dict[s[i]];
        if(tmp_char==="0"){
            tmp_s.push(s[i]);
        }else{
            if(dict[s[i]]!=tmp_s.pop()){
                return(false);
            };
        };
    };
    if(tmp_s.length===0){
        return(true);
    }else{
        return(false);
    };
};

var isValid_2 = function(s) {// other solution
    var i=0;
    var tmp_stack =[];
    for(i=0;i<s.length;i++){
        switch(s[i]){
            case "(":
                tmp_stack.push(s[i]);
                break;
            case "{":
                tmp_stack.push(s[i]);
                break;
            case "[":
                tmp_stack.push(s[i]);
                break;
            case ")":
                if(tmp_stack.pop()!="("){
                    return(false);
                };
                break;
            case "}":
                if(tmp_stack.pop()!="{"){
                    return(false);
                };
                break;
            case "]":
                if(tmp_stack.pop()!="["){
                    return(false);
                };
                break;
        };
    };
    if(tmp_stack.length===0){
        return(true);
    }else{
        return(false);
    };  
};

var string_example ="{[]}";
console.log(isValid(string_example));