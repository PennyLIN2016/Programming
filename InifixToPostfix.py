#from StackClass import StackClass
def infixtopostfix(infixexpr):

    s=[]
    outlst=[]
    prec={}
    prec['/']=3
    prec['*']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1

    tokenlst = infixexpr.split()
    print tokenlst
    for token in tokenlst:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outlst.append(token)
        elif token == '(':
            s.append(token)
        elif token == ')':
            topToken=s.pop()
            while topToken != '(':
                outlst.append(topToken)
                topToken=s.pop()
        else:
            while (len(s)!= 0) and (prec[s[-1]] >= prec[token]):
                # compare the priority of operators
                outlst.append(s.pop())
            s.append(token)

    while len(s)!= 0:
        # push all left operation in the end of the list
        opToken=s.pop()
        outlst.append(opToken)
    return " ".join(outlst)

print (infixtopostfix("A *  B + C * D"))


