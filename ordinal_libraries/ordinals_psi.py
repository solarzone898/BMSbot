# Supports countable ordinals up to ψ₀(I(1,0))
# Important: I_x+y is assumed to be {x,y}
# I_x*(n+1) = I_x+I_x*n = {x,I_x*n}
from functools import total_ordering # psi v1.5½ patch 1
@total_ordering
class Ordinal:
    def __init__(self,I_subscript=0,subscript=0,arg=1,copies=1,addend=0):
        self.Isub=I_subscript
        self.sub=subscript
        self.arg=arg
        self.copies=copies
        self.addend=addend
    def copy(self):
        return Ordinal(self.Isub, self.sub, self.arg, self.copies, self.addend)
    def __repr__(self):
        return str(self)
    def __str__(self):
        term=''
        if self.arg==0:
            if self.Isub==0:
                if isinstance(self.sub, int):
                    term= 'Ω' +''.join(['₀₁₂₃₄₅₆₇₈₉'[int(i)] for i in str(self.sub)]) * (self.sub != 1) #ψ_α(0) = Ω_α
                else:
                    if omega(self.Isub,0)+self.sub>=omega(self.Isub+1,0):
                        term= 'Ω_' +'{' * (self.sub != w) + str(self.sub) + '}' * (self.sub != w)
                    else:
                        term = 'Ω_' + '{0,' + str(self.sub) + '}'
            elif self.Isub>0:
                if self.sub==0:
                    if isinstance(self.Isub, int):
                        term = 'I' + ''.join(['₀₁₂₃₄₅₆₇₈₉'[int(i)] for i in str(self.Isub)]) * (self.Isub != 1)  # ψ_α(0) = Ω_α
                    else:
                        term = 'I_' + '{' * (self.Isub != w) + str(self.Isub) + '}' * (self.Isub != w)
                else:
                    if get_tuple_2(omega(self.Isub,0))<get_tuple_2(self.sub) and (self.Isub,self.sub)>=(0,I):
                        term=f'Ω_{{{str(self.Isub)+","+str(self.sub)}}}'
                    else:
                        term = f'Ω_{{{omega(self.Isub,0)+self.sub}}}'
        elif self.sub==0 and self.Isub==0:
            if isinstance(self.arg,int):
                term= 'ω'+''.join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(i)] for i in str(self.arg)])*(self.arg!=1) #ψ_0(α) = ω^α
            else:
                if self.arg<W:
                    try:
                        divW(self.arg.arg)
                        if self.arg.arg>=psi(1,W):
                            raise Exception('qwertyuiop')
                        term= str(self.arg)
                    except:
                        term= f'ω^{"("*(self.arg!=w)}{self.arg}{")"*(self.arg!=w)}'
                else:
                    try:
                        divW(self.arg)
                        if self.arg<psi(1, W):
                            if self.arg<psi(1, 1):
                                term= 'ε' + ''.join(['₀₁₂₃₄₅₆₇₈₉'[int(i)] for i in str(self.arg.copies-1)])
                            else:
                                x = divW(self.arg)  # epsilon index (dividing by Ω)
                                term= f'ε_{"{"*(x!=w)}{x}{"}"*(x!=w)}'
                        else:
                            raise Exception('qwertyuiop')
                    except:
                        if self.arg.addend==0 or self.arg.addend>=W:
                            try:
                                if self.arg.addend==0:
                                    raise Exception('defrmgtnrfyifrtgnmrefr')
                                a=divW(self.arg.addend)
                                a=norm(a)
                                try:
                                    b=a.copy()
                                except:
                                    b=a

                                if a<W:
                                    if psi(0, Ordinal(self.Isub, self.arg.sub, self.arg.arg, self.arg.copies)) + a > psi(0,Ordinal(self.arg.Isub,self.arg.sub,self.arg.arg,self.arg.copies) + 1):
                                        if self >= psi(0,Ordinal(self.arg.Isub, self.arg.sub, self.arg.arg, self.arg.copies) + psi(1, W)):
                                            term = f'ψ₀({self.arg})'
                                        else:
                                            term = f'ε_{{{b}}}'
                                    else:
                                        if self >= psi(0,Ordinal(self.arg.Isub, self.arg.sub, self.arg.arg, self.arg.copies) + psi(1, W)):
                                            term = f'ψ₀({self.arg})'
                                        else:
                                            term = f'ε_{{{psi(0, Ordinal(self.arg.Isub, self.arg.sub, self.arg.arg, self.arg.copies)) + b}}}'
                                else:
                                    raise Exception('werfghrtnewdbuyrgthfwde')
                            except:
                                if self.arg >= Ordinal(0, 1, W, 2, 0):
                                    try:
                                        if getaddend(self.arg)>0:
                                            term = f'ω^(ε_{{{psi(0, Ordinal(self.arg.Isub, self.arg.sub, self.arg.arg, self.arg.copies))+norm(divW(removeaddend(self.arg).addend))}}}+{getaddend(self.arg)})'
                                        else:
                                            raise Exception('sderfgtyhujk')
                                    except:
                                        term = f'ψ₀({self.arg})'
                                else:
                                    if self.arg==Ordinal(0, 1, W, 1, 0):
                                        term= 'ζ₀'
                                    else:
                                        x = self.arg.copy()
                                        x.addend = 0
                                        if self.arg.addend >= psi(0,Ordinal(self.arg.Isub, self.arg.sub, self.arg.arg, self.arg.copies,1)):
                                            if getaddend(self.arg)!=0:
                                                term = f'ω^(ε_{{{z0+norm(divW(removeaddend(self.arg).addend))}}}+{getaddend(self.arg)})'
                                            else:
                                                term = f'ε_{{{z0+norm(divW(removeaddend(self.arg).addend))}}}'
                                        else:
                                            term = f'ω^({psi(0, x) + self.arg.addend})'
                        else:
                            x=self.arg.copy()
                            x.addend=0
                            if self.arg.addend>=psi(0,Ordinal(self.arg.Isub, self.arg.sub,self.arg.arg,self.arg.copies,1)):
                                term= f'ω^({self.arg.addend})'
                            else:
                                term= f'ω^({psi(0,x)+self.arg.addend})'
        else:
            if self.arg>omega(self.Isub,self.sub+1):
                if isinstance(self.sub, int) and self.Isub==0:
                    term= 'ψ' +''.join(['₀₁₂₃₄₅₆₇₈₉'[int(i)] for i in str(self.sub)]) + '(' + str(self.arg) + ')'
                else:
                    if omega(self.Isub,0)+self.sub>=omega(self.Isub+1,0):
                        term= 'ψ_' +'{' * (omega(self.Isub,0)+self.sub != w) + str(self.Isub)+','+str(self.sub) + '}' * (omega(self.Isub,0)+self.sub != w) + '(' + str(self.arg) + ')'
                    else:
                        term = 'ψ_' + '{' * (omega(self.Isub, 0) + self.sub != w) + str(omega(self.Isub,0)+self.sub)+ '}' * (omega(self.Isub, 0) + self.sub != w) + '(' + str(self.arg) + ')'
            else:
                term= f'ω^({psi3(self.Isub, self.sub, 0) + self.arg})'
        if self.copies!=1:
            term+=f'·{self.copies}'
        if self.addend!=0:
            term+=f'+{self.addend}'
        term=term.replace('ψ₀(ω^(ω^(Ω·2)))','Γ₀')
        term=term.replace('Ω_{0,I}','Λ')
        return term
    def as_tuple(self):
        return (self.Isub ,self.sub, self.arg, self.copies, self.addend)
    def __eq__(self,other):
        if isinstance(other,Ordinal):
            return self.as_tuple() == other.as_tuple()
        return False
    def __lt__(self,other):
        if isinstance(other,Ordinal):
            return self.as_tuple()<other.as_tuple()
        return False
    def __add__(self,other):
        if isinstance(other,Ordinal):
            if (self.Isub,self.sub,self.arg)<(other.Isub,other.sub,other.arg):
                return other
            else:
                if (self.Isub,self.sub,self.arg)==(other.Isub,other.sub,other.arg):
                    k=self.copy()
                    k.copies+=other.copies
                    k.addend+=other.addend
                    return k
                else:
                    k=self.copy()
                    k.addend+=other
                    return k
        else:
            k=self.copy()
            k.addend+=other
            return k
    def __radd__(self,other):
        return self
def omega(n,k):
    if (n,k)==(0,0):
        return 0
    return Ordinal(n,k,0)
def psi(n,k):
    if (n,k)!=(0,0):
        return Ordinal(0,n,k)
    return 1
def psi3(n,k,r):
    if (n,k,r)!=(0,0,0):
        return Ordinal(n,k,r)
    return 1
def divW(k):
    if k!=0:
        if k<psi(1,1):
            if k.sub<1:
                raise Exception('you can\'t do that')
            return k.copies+divW(k.addend)
        else:
            if k<omega(0,2):
                return Ordinal(0,0,k.arg,k.copies,0)+divW(k.addend)
            raise Exception('sedtgyhntruwertihnvfn c')
    return 0
def getaddend(k):
    if k<W:
        return k
    else:
        return getaddend(k.addend)
def removeaddend(k):
    if k<W:
        return 0
    else:
        return Ordinal(k.Isub, k.sub, k.arg, k.copies) + removeaddend(k.addend)
def removeaddend1(k):
    if k<psi(1,W):
        return 0
    else:
        return Ordinal(k.Isub, k.sub, k.arg, k.copies) + removeaddend1(k.addend)
def get_tuple_2(k):
    x = (k.Isub,k.sub,k.arg) if isinstance(k,Ordinal) else (-1,0,0); return x
def norm(n):
    try:
        if W > n.arg >= psi(0, W):
            n = n.arg
        else:
            n = n
    except:
        n = n
    return n
def aslatex(self):
    if type(self)==int:
        return str(self)
    term = ''
    if self.arg == 0:
        if self.Isub == 0:
            if self.sub < L:
                term = '\Omega' + ('_{' + aslatex(self.sub) + '}')*(self.sub>1)
            else:
                term = '\Omega' + '_{0,' + aslatex(self.sub) + '}'
        elif self.Isub > 0:
            if self.sub == 0:
                term = 'I' + ('_{'+aslatex(self.Isub) + '}')*(self.Isub>1)
            else:
                term = f'\Omega_{{{aslatex(self.Isub) + "," + aslatex(self.sub)}}}'
    elif self.sub == 0 and self.Isub == 0:
        if self.arg < W:
            if self.arg!=1:
                term = f'\omega^{{{aslatex(self.arg)}}}'
            else:
                term = f'\omega'
        else:
            try:
                divW(self.arg)
                if self.arg < psi(1, W):
                    x = divW(self.arg)  # epsilon index (dividing by Ω)
                    try:
                        x-=1
                    except:
                        pass
                    term = f'\\varepsilon_{{{aslatex(x)}}}'
                else:
                    raise Exception('qwertyuiop')
            except:
                if self.arg.addend == 0 or self.arg.addend >= W:
                    if self.arg >= Ordinal(0, 1, W, 2, 0):
                        term = f'\psi_0({aslatex(self.arg)})'
                    else:
                        if self.arg == Ordinal(0, 1, W, 1, 0):
                            term = '\zeta_0'
                        else:
                            term = f'\psi_0({aslatex(self.arg)})'
                else:
                    term = f'\psi_0({aslatex(self.arg)})'
    else:
        if self.arg>omega(self.Isub,self.sub+1):
            if self.Isub>0:
                term=f'\psi_{{{aslatex(self.Isub)},{aslatex(self.sub)}}}({aslatex(self.arg)})'
            else:
                term = f'\psi_{{{aslatex(self.sub)}}}({aslatex(self.arg)})'
        else:
            term = f'\omega^{{{aslatex(psi3(self.Isub, self.sub, 0) + self.arg)}}}'
    if self.copies != 1:
        term += f'\\cdot {self.copies}'
    if self.addend != 0:
        term += f'+{aslatex(self.addend)}'
    term = term.replace('\psi_0(\omega^{\omega^{\Omega\cdot2}})', '\Gamma_0')
    term = term.replace('\Omega_{0,I}', '\Lambda')
    return term
w=Ordinal()
W=omega(0,1)
I=omega(1,0)
L=omega(0,I)
e0=psi(0,W)
z0=psi(0,psi(1,W))
