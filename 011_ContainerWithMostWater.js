/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var r = 0, l = height.length-1;
    var max_area = 0;

    while (r<l){
        if (height[r]>height[l]){
            max_area = Math.max(max_area,(height[l])*(l-r));
            l--;
        }else{
            max_area = Math.max(max_area,(height[r])*(l-r));
            r++;
        };
    };
    return(max_area);    
};



var in_example = [1,8,6,2,5,4,8,3,7];

console.log(maxArea(in_example));