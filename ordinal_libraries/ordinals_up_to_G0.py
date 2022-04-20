from functools import total_ordering
 
# derived from https://github.com/ajcr/transfinite/blob/master/transfinite/ordinal.py
# most of the multiplication and exponentiation code is from https://reinhardt-c.github.io/VebleNum.js/
# Goes up to Γ₀, for higher ordinals only addition is supported, in ordinals_psi.py
@total_orderingdef is_finite_ordinal(a):
    """
    Return True if n is a finite ordinal (non-negative int).
    """
    return isinstance(a, int) and a >= 0
def isSum(a):
    return a.addend!=0
def isProd(a):
    return a.addend==0 and a.copies>1
def isPhi(a):
    return a.addend==0 and a.copies==1
def exp(x, n):
    """
    Compute x**n using exponentiation by squaring.
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return exp(x * x, n // 2)
    return exp(x * x, (n - 1) // 2) * x
 
 
class OrdinalConstructionError(Exception):
    pass
 
 
@total_ordering
class Ordinal:
 
    def __init__(self, subscript=0, arg=0, copies=1, addend=0):
       
        '= ϕ(subscript,arg)^exponent*copies+addend'
        self.subscript = subscript
        self.arg = arg
        self.copies = copies
        self.addend = addend
    def is_limit(self):
        """
        Return true if ordinal is a limit ordinal.
        """
        if is_finite_ordinal(self.addend):
            return self.addend == 0
        return self.addend.is_limit()
 
    def is_successor(self):
        """
        Return true if ordinal is a successor ordinal.
        """
        return not self.is_limit()
    def __eq__(self, other):
        if isinstance(other, Ordinal):
            return self.as_tuple() == other.as_tuple()
        return False
 
    def __lt__(self, other):
        if isinstance(other, Ordinal):
            if self.veblen()==other.veblen():
                return self.as_tuple()[2:]<other.as_tuple()[2:]
            else:
                return compare_veblen(self.veblen()[0],self.veblen()[1],other.veblen()[0],other.veblen()[1])
        if is_finite_ordinal(other):
            return False
        return NotImplemented
    def __repr__(self):
        return str(self)
 
    def __str__(self):
        term = "φ"
        if self.subscript<4:
            term='ωεζη'[self.subscript]
            if 0<self.subscript<4:
                term+=f'{"_{"*(1-is_finite_ordinal(self.arg))}{self.arg}{"}"*(1-is_finite_ordinal(self.arg))}'
            else:
                if self.arg>1:
                    if (
                            is_finite_ordinal(self.arg)
                            or self.arg.copies == 1
                            and self.arg.addend == 0
                            and self.arg.subscript == 0
                    ):
                        term += f"^{self.arg}"

                    else:
                        term += f"^({self.arg})"
        else:
            term+=f'_{{{self.subscript}}}({self.arg})'
 
        if self.copies != 1:
            term += f"*{self.copies}"
 
        if self.addend != 0:
            term += f"+{self.addend}"
 
        return term

    def __hash__(self):
        return hash(self.as_tuple())
 
    def __eq__(self, other):
        if isinstance(other, Ordinal):
            return self.as_tuple() == other.as_tuple()
        return False
 
    def __add__(self, other):
 
        if not is_ordinal(other):
            return NotImplemented
 
 
        if is_finite_ordinal(other) or compare_veblen(other.veblen()[0],other.veblen()[1],self.veblen()[0],self.veblen()[1]):
            return Ordinal(self.subscript, self.arg, self.copies, self.addend + other)
 
 
        if (self.veblen()==other.veblen()):
            return Ordinal(self.subscript, self.arg, self.copies + other.copies, other.addend)
 
 
        return other
 
    def __radd__(self, other):
        if not is_finite_ordinal(other):
            return NotImplemented
 
        # n + a == a
        return self
 
    def __mul__(self, other):
 
        if not is_ordinal(other):
            return NotImplemented
 
        if other == 0:
            return 0
        if is_finite_ordinal(other):
            return Ordinal(self.subscript, self.arg, self.copies * other, self.addend)
        if isSum(other):
            return self * Ordinal(other.subscript, other.arg, other.copies, 0) + self * other.addend
        if isSum(self):
            if not is_finite_ordinal(other):
                return Ordinal(self.subscript,self.arg,self.copies,0)*other
            t=Ordinal(self.subscript,self.arg,self.copies,0)
            return t*other+self.addend
        elif isProd(self):
            return Ordinal(self.subscript,self.arg,1)*other
        elif isPhi(self):
            if isProd(other):
                return self * Ordinal(other.subscript, other.arg, 1) * other.copies
            return Ordinal(0,ns(self)+ns(other))
    def __rmul__(self, other):
 
        if not is_finite_ordinal(other):
            return NotImplemented
 
        if other == 0:
            return 0
        return self

    def __pow__(self, other):
 
        if not is_ordinal(other):
            return NotImplemented
        if is_finite_ordinal(other):
            return exp(self, other)
        if isSum(other):
            return self ** Ordinal(other.subscript, other.arg, other.copies) * self ** other.addend
        if isProd(other):
            return (self ** Ordinal(other.subscript, other.arg)) ** other.copies
        if isSum(self):
            return Ordinal(self.subscript, self.arg,self.copies)**other
        if isProd(self):
            return Ordinal(self.subscript, self.arg)**other
        if isPhi(self):
            return Ordinal(0,ns(self)*other)
    def __rpow__(self, other):
        s=other
        o=self
        if isSum(o):
            return s**Ordinal(o.subscript,o.arg,o.copies)*s**o.addend
        if isProd(o):
            return s**Ordinal(o.subscript,o.arg)**o.copies
        if o.veblen()[0]==0 and 1<((o.subscript,)*(o.subscript>0))[0]:
            if w<=((o.subscript,)*(o.subscript>0))[0]:
                return Ordinal(0,o)
            k=o
            if k.subscript>0:
                k.subscript-=1
            else:
                k.arg-=1
            return Ordinal(0,k)
        return o
    def as_tuple(self):
        return (self.subscript,self.arg,self.copies,self.addend)
    def veblen(self):
        return (self.subscript,self.arg)
 
def is_ordinal(a):
    """
    Return True if a is a finite or infinite ordinal.
    """
    return is_finite_ordinal(a) or isinstance(a, Ordinal)
def e(a):
    return Ordinal(1,a)
def z(a):
    return Ordinal(2,a)
def n(a):
    return Ordinal(3,a)
def phi(a,b=None):
    if b==None:
        if a!=0:
            return Ordinal(0,a)
        return 1
    if (a,b)!=(0,0):
        x=Ordinal(a,b)
        return x
    return 1
def compare_veblen(a,b,c,d):
    if (a==c and b<d) or (a<c and b<Ordinal(c,d)) or (a>c and Ordinal(a,b)<d):
        return True
    return False
def as_latex(a):
    if not type(a)==Ordinal:
        if type(a)==float and 'e' in str(a):
            return str(a).split('e')[0]+'\\times 10^{'+str(a).split('e')[1].replace('+','')+'}'
        else:
            return str(a)
    else:
        term=r'\varphi'
        if a.subscript<4:
            term=(r'\omega',r'\varepsilon',r'\zeta',r'\eta')[a.subscript]
            if 0<a.subscript<4:
                term+=f'_{{{as_latex(a.arg)}}}'
            else:
                if a.arg > 1:
                    term+=f"^{{{as_latex(a.arg)}}}"
        else:
            term+=f'_{{{as_latex(a.subscript)}}}({as_latex(a.arg)})'
 
        if a.copies != 1:
            term += f"\\cdot{a.copies}"
 
        if a.addend != 0:
            term += f"+{as_latex(a.addend)}"
 
        return term
def ns(a):
    if a.subscript==0:
        return a.arg
    else:
        return a
def is_successor(a):
    if isinstance(a,Ordinal):
        return a.is_successor()
    return a>0
def is_limit(a):
    if isinstance(a,Ordinal):
        return a.is_limit()
    return a==0
w=Ordinal(0,1)
