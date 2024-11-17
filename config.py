

QUESTION_IMG_SIZE = 640

SYMBOLS_IMG_SIZE = 45

SYMBOLS = ['0','1','2','3','4','5','6','7','8','9',',',
           'a', 'b', 'c', 'x', 'y', 'z', 'p', 'q', 'r', 's',
            '-','+','*','/','=','int','d','infty',
            'cos','x','sin','log','e','lim','rightarrow',
            'pi','(',')','.','sqrt','tan']

TOKEN_TYPE = {'OPERATOR':0,'DIGIT':1,'FUNCTION':2,
              'VARIABLE':3,'CMP':4,'RESERVE':5,
              'DECIMAL_POINT':6,'END':7,'SPECIAL':8}

OPERATOR = ['+','-','times','div','sqrt']
DIGIT = ['0','1','2','3','4','5','6','7','8','9']
FUNCTION = ['cos','sin','log','tan','lim']
VARIABLE = ['a', 'b', 'c', 'x', 'y', 'z', 'p', 'q', 'r', 's',]
CMP = ['=','<','>','le','ge']
RESERVE = ['e','pi','infty']
SPECIAL = ['(',')','d',',','rightarrow']