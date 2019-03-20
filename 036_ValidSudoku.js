/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var list_1 = new Array(9),// row visited: false not  ture yes
        list_2 = new Array(9),// col visited: false not  ture yes
        list_3 = new Array(9);// block visited: false not  ture yes

    for (var d = 0; d < 9; d++) {
        list_1[d] = new Array(9);
        list_1[d].fill(0);
        list_2[d] = new Array(9);
        list_2[d].fill(0);
        list_3[d] = new Array(9);
        list_3[d].fill(0);
    };


    console.log('list_1 : ');
    console.log(list_1);
    console.log('list_2 : ');
    console.log(list_2);
    console.log('list_3 : ');
    console.log(list_3);
    
    
    for (var i = 0;i<9; i++){
        for(var j = 0;j<9;j++){
            var tmp = board[i][j];
            if (tmp ==="."){
                continue;
            };
            if(list_1[i][tmp - 1] + list_2[tmp - 1][j] + list_3[Math.floor(i / 3) * 3 +Math.floor(j / 3)][tmp - 1]>0){

                return(false);
            };
            list_1[i][tmp - 1] = 1;
            list_2[tmp - 1][j] = 1;
            list_3[Math.floor(i / 3) * 3 + Math.floor(j / 3)][tmp - 1] = 1;
        };
    };
    return(true);
};

var in_list =[
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
];


//console.log(in_list);
console.log(isValidSudoku(in_list));
console.log('-----------the end!----------------');