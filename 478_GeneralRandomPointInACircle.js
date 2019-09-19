/**
 * @param {number} radius
 * @param {number} x_center
 * @param {number} y_center
 */
//Runtime: 168 ms, faster than 71.43% of JavaScript online submissions for Generate Random Point in a Circle.
//Memory Usage: 62.8 MB, less than 100.00% of JavaScript online submissions for Generate Random Point in a Circle.
var Solution = function(radius, x_center, y_center) {
    this.r=radius;
    this.x=x_center;
    this.y=y_center;
};

/**
 * @return {number[]}
 */
Solution.prototype.randPoint = function() {
    var rr=Math.sqrt(Math.random())*this.r
    var alphe= Math.random()*Math.PI*2;
    return[this.x+rr*Math.cos(alphe),this.y+rr*Math.sin(alphe)];   
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(radius, x_center, y_center)
 * var param_1 = obj.randPoint()
 */

var obj = new Solution(1, 2, 2);
var param_1 = obj.randPoint();
console.log(param_1);