from pyparsing import Word, Literal, Or, nums, Forward, StringEnd
from operator import mul, div, add, sub

class NumNode(object):
    def __init__(self, t):
        self.num = float(t[0])        
    def calc(self):
        return self.num          
    def __repr__(self):
        return 'Num(%s)' % self.num
        
class OpNode(object):
    def __init__(self, t):               
        self.left = t[0]
        self.op = { '-' : sub, '+' : add, '/' : div, '*' : mul }[t[1]]
        self.right = t[2]       
    def calc(self):
        return self.op(self.left.calc(), self.right.calc())        
    def __repr__(self):
        return 'Op(%s, %s, %s)' % (self.left, self.op, self.right)

plus = Literal('+')
minus = Literal('-')
div = Literal('/')
mult = Literal('*')
        
factor = Word(nums).setParseAction(NumNode)

term = Forward()
term << (( factor + (mult | div) + term ).setParseAction(OpNode) | factor )        

expr = Forward()
expr << ((term + (plus | minus) + expr).setParseAction(OpNode) | term )

start = expr + StringEnd()

if __name__ == '__main__':
    tree = start.parseString('2 * 4 + 6 * 7')[0]
    print tree
    print tree.calc()
    
    

