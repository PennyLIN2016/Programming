// 
var checkedArray = new Array(9)
var isValidSudoku = function(board) {

    for (var i = 0 ; i < board.length ; i++)
    {
       checkedArray.fill(0)
        for(var j = 0 ; j < board.length ; j ++)
        {
            if (checkValue(board[i][j]) === false )
            {

                return false
            }
        }

    }



    for ( i = 0 ; i < board.length ; i++)
    {
         checkedArray.fill(0)
        for( j = 0 ; j < board.length ; j++)
        {
            if (checkValue(board[j][i]) === false )
            {

                return false
            }
        }
    }

    checkedArray.fill(0)

    for ( i = 0 ; i < board.length ; i+=3)
    {

        for( j = 0 ; j < board.length ; j+=3)
        {
             checkedArray.fill(0)

            for (var k = 0 ; k < 9; k++)
            { 
               // console.log("checking "+i+ k/3+" , "+j + k%3)
                if (checkValue(board[i+   Math.floor(k/3)][j + k%3]) === false )
                {

                  return false
                }

            }
        }
    }

   return true;

};

var checkValue = function(value)
{
      // console.log("checking value "+value)

    if(value == '.') //根据题意不校验
    {   
        return  true;
    }

    var index = value - '1';
    if (index < 0 || index > 9 ||  checkedArray[index] > 0)
    {
     // console.log("value is "+index +"/" +checkedArray[index])
        return false;
    }
    else
    {
   // console.log("push index is "+index)
        checkedArray[index] = 1;
    }

    return true;
}