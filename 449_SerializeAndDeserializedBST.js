
 // Definition for a binary tree node.
function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
}
 
//Runtime: 84 ms, faster than 64.15% of JavaScript online submissions for Serialize and Deserialize BST.
//Memory Usage: 40.6 MB, less than 100.00% of JavaScript online submissions for Serialize and Deserialize BST.
/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    if(!root){
        return ''
    };
    var left=serialize(root.left);
    var right=serialize(root.right);
    var res= root.val.toString();
    if(left){res+='_'+left};
    if(right){res+='_'+right};
    return res
};
var deSlide = function(nodes,start,end) {
    if(start>end){return null};
    var root= new TreeNode(parseInt(nodes[start],10));
    for(var i=start+1;i<=end&&(parseInt(nodes[i])<root.val);i++){};       
    root.left=deSlide(nodes,start+1,i-1);      
    root.right=deSlide(nodes,i,end);
    return root;
};


/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if(!data){return null};
    var nlist=data.split('_');
    return deSlide(nlist,0,nlist.length-1)

};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
var n1=new TreeNode(2);
var n2=new TreeNode(1);
var n3=new TreeNode(3);
n1.left=n2;
n1.right=n3;
var strdate= serialize(n1);
console.log(strdate);
var n= new TreeNode(0);
n=deserialize(strdate)
