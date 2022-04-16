# converts ordinals to strings interpretable by http://www.madore.org/~david/math/drawordinals.html
from ordinals import *
def getcnf(ord):
    if isinstance(ord, int):
        return [0,ord]*(ord!=0)
    if ord.subscript==1:
        return getcnf(ord.addend)+[e(ord.arg),ord.copies]
    return getcnf(ord.addend)+[ord.exponent,ord.copies]
def toString(ord):
    if ord>=z(0):
        raise Exception
    else:
        if ord<w:
            return f'oo0.{ord}.'
        elif ord.subscript==1 and ord.addend==0:
            return f'e{toString(ord.arg)}'
        cnf = getcnf(ord)
        a=''
        for i in range(0,len(cnf),2):
            a+=f'o{toString(cnf[i])}{cnf[i+1]}'
            if i==len(cnf)-2:
                a+='.'
        return a
while True:
    x=eval(input('Ordinal to display> ').replace('^','**'))
    print(f'http://www.madore.org/~david/math/drawordinals.html#?v={toString(x)}&i=0&l=')
