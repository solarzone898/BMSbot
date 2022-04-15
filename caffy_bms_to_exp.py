# https://googology.fandom.com/wiki/User_blog:Ytosk/Algorithm_that_changes_BMS_matrices_into_ordinals_up_to_SRO
# but better
#---------------------------------------------------
# solarzone's ordinal library
from functools import total_ordering # psi v1.3½ patch 1
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
                    if self.sub.Isub==0 and self.sub<L:
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
                    if self.sub>omega(self.Isub,0):
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
            if self>=psi3(self.Isub,self.sub,psi3(self.Isub,self.sub,1)):
                if isinstance(self.sub, int) and self.Isub==0:
                    term= 'ψ' +''.join(['₀₁₂₃₄₅₆₇₈₉'[int(i)] for i in str(self.sub)]) + '(' + str(self.arg) + ')'
                else:
                    if self.sub>omega(self.Isub,0) and (self.Isub,self.sub)>=(0,I):
                        term= 'ψ_' +'{' * (omega(self.Isub,0)+self.sub != w) + str(self.Isub)+','+str(self.sub) + '}' * (omega(self.Isub,0)+self.sub != w) + '(' + str(self.arg) + ')'
                    else:
                        term = 'ψ_' + '{' * (omega(self.Isub, 0) + self.sub != w) + str(omega(self.Isub,0)+self.sub)+ '}' * (omega(self.Isub, 0) + self.sub != w) + '(' + str(self.arg) + ')'
            else:
                term= f'ω^({psi3(self.Isub, self.sub, 0) + self.arg})'
        if self.copies!=1:
            term+=f'·{self.copies}'
        if self.addend!=0:
            term+=f'+{self.addend}'
        term=term.replace('ψ₀(ψ₁(ψ₁(Ω)))','Γ₀')
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
                k=other
                if isinstance(self,Ordinal):
                    k.addend=self+k.addend
                else:
                    k.addend=k.addend+self
                return k
            else:
                if self.Isub==other.Isub and self.sub==other.sub and self.arg==other.arg:
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
def norm(n):
    try:
        if W > n.arg >= psi(0, W):
            n = n.arg
        else:
            n = n
    except:
        n = n
    return n
w=Ordinal()
W=omega(0,1)
I=omega(1,0)
L=omega(0,I)
e0=psi(0,W)
z0=psi(0,psi(1,W))
#make it natural number
#input :X=list [a,b,c,d]
#output:natural number (-1 is it's not standard for natural number)
def tonat(X):
  if type(X) is int:
    return X
  if X==[]:
    return 0
  elif type(X) is list and len(X)==4:
    if X[0]==[] and X[1]==[] and X[2]==[] and tonat(X[3])!=-1:
      return tonat(X[3])+1
  return -1
#---------------------------------------------------
#make it string of psi function
#input :X=list [a,b,c,d]
#output:string "p_a(b)+c" with more sugar syntax
def tosugar(X):
  # print(tosolarzone(X,obsfucate=True))
  # if tonat(X)>-1:
  #     return tonat(X)
  if X==[]:
      return 0
  return psi3(tosugar(X[0]),tosugar(X[1]),tosugar(X[2]))+tosugar(X[3])
def tosolarzone(X,obsfucate=False):
    if obsfucate:
        if X==[]:
            return '0'
    else:
        if tonat(X)>-1:
            return str(tonat(X))
    if X[0]==[]:
        return f'({f"{tosolarzone(X[1],obsfucate)},"*(X[1]!=[])}{tosolarzone(X[2],obsfucate)}){f"{tosolarzone(X[3],obsfucate)}" * (X[3] != [])}'
    else:
        if X[1]==[]:
            if X[2]==[]:
                return f'({tosolarzone(X[0],obsfucate)})I{f"{tosolarzone(X[3],obsfucate)}" * (X[3] != [])}'
            else:
                return f'(({tosolarzone(X[0],obsfucate)})I,{tosolarzone(X[2],obsfucate)}){f"{tosolarzone(X[3],obsfucate)}" * (X[3] != [])}'
        else:
            return f'(({tosolarzone(X[0],obsfucate)})I{tosolarzone(X[1],obsfucate)},{tosolarzone(X[2],obsfucate)}){f"{tosolarzone(X[3],obsfucate)}" * (X[3] != [])}'
len_=None
def P(M,r,n):
    if r==-1:
        return n-1
    else:
        ret=P(M,r-1,n)
        while ret>-1 and M[ret][r]>=M[n][r]:
            ret=P(M,r-1,ret)
        return ret
def U(M,n):
    # Upgrading type,source of M[n]
    # (0,None): Not upgraded
    # Condition: n is last column, M[n][2]=1 (overriding others), other cases don't
    #  trigger
    # Set m to 0-ancestor of n that is 0,1,2-child of the 1-parent
    # (should be the lowest possible column that can upgrade, ^ seems to match that)
    # (1,n+1): Upgraded by following ((0,0,0)(1,1,1)(2,1,0)(1,1,1))
    # Condition: M[n+1]=M[m]
    # (2,m): Upgraded by ancestor m, simple case ((0,0,0)(1,1,1)(2,1,0)(2,0,0))
    # Condition: M[n+1][0]>M[m][0]
    # (3,m): Upgraded by ancestor m, Wfp case ((0,0,0)(1,1,1)(2,1,1)(3,1,0)(2,0,0))
    # Condition: Same as 2, but last child of m before n has third row 1
    if len(M)==n+1 or M[n][2]==1:
        return 0,None
    m=n
    while m>-1:
        cm=m
        m=P(M,0,m)
        if P(M,0,m)==P(M,1,n)>-1 and M[m]==[i+1 for i in M[P(M,0,m)]]:
            if M[n+1][0]>M[m][0]:
                if M[cm][2]==1:
                    return 3,m
                else:
                    return 2,m
            if M[n+1]==M[m]:
                return 1,n+1
    return 0,None
def pv(M,n):
    # Value of an upgrader, and only that
    # w^(1+the sum of mv(M,k) for any children k with third row 1),
    # at the appropriate inacc level
    sus=0
    ret=[[],[],[],[]]
    for m in range(n+1,len(M)):
        if P(M,0,m)==n and M[m][2]==1:
            e,p=mv(M,m)
            sus+=e
            if e==0:
                ret=add(ret,p)
    if sus==1:
        return exp(ret),[]
    return [],exp(ret)
def mv(M,n):
    # Contribution of a third-row-1 child of an upgrader
    # 0,x=multiply by w^x
    # 1,x=increase _-inacc level by x (only x=1 is possible until w-inaccs)
    # x=w^(sum of o(M,children of n))
    effect=0
    ret=[]
    for m in range(n+1,len(M)):
        if P(M,0,m)==n:
            if M[m][2]==1:
                effect=1
            else:
                ret=add(ret,o(M,m))
    return effect,exp(ret)
def v(M,n):
    # Return subscripts for o(M,n)
    # Third row=0:
    # Check upgrading of column n:
    # No upgrading: 1-parent with W-subscript incremented, if no 1-parent then 0
    # Upgraded by ancestor, Wfp case: ^ but I-subscript
    # Other cases: Copy upgrader value
    if M[n][2]==0:
        ut,up=U(M,n)
        if ut==0:
            if P(M,1,n)>-1:
                a,b=v(M,P(M,1,n))
                return a,add(b,[[],[],[],[]])
            return [],[]
        elif ut==3:
            if P(M,1,n)>-1:
                a,b=v(M,P(M,1,n))
                return add(a,[[],[],[],[]]),[]
            return [[],[],[],[]],[]
        else:
            return v(M,up)
    # Third row=1:
    # (2-parent value if any else 0)+pv(M,n)
    else:
        p,q=pv(M,n)
        if P(M,2,n)>-1:
            a,b=v(M,P(M,2,n))
            return add(a,p),add(b,q) if p==[] else q
        return p,q
def o(M,n):
    # psi_v(M,n) of sum of o(M,k) of children, excluding:
    # 1. Same second row as previous, third row 1, previous third row 0,
    #  exists m between k-1 and 1-parent s.t. M[m]=M[k],
    #  all children of k have third row 1
    #  (pure upgrader)
    # 2. 1, but the last descendant of k is [M[k][0]+1,0,0] (overriding the
    #  third row 1 condition) and it upgrades previous column which follows
    #  third-row-0 case 4
    #  (self-upgrading pure upgrader)
    # 3. Third row 1 if third row of n is 1
    #  (W_(w^x) children)
    # 4. [M[n][0]+1,0,0] if that upgrades previous column which follows
    #  third-row-0 case 4
    #  (Wfp)
    ret=[]
    for k in range(len(M)):
        if P(M,0,k)!=n:
            continue
        if M[k][1]==M[k-1][1] and M[k][2]>M[k-1][2]:
            upg=0
            for j in range(P(M,1,k-1),k):
                if M[j]==M[k]:
                    upg=1
                    break
            for l in range(k,len(M)):
                if P(M,0,l)==k and M[l][2]==0:
                    if len(M)==l+1 or M[l+1][0]<=M[n][0]:
                        if U(M,l-1)==(3,k) and M[l]==[M[k][0]+1,0,0]:
                            continue
                    upg=0
                    break
            if upg:
                continue
        if M[n][2]==M[k][2]==1:
            continue
        if M[k]==[M[n][0]+1,0,0] and (len(M)==k+1 or P(M,0,k+1)<k):
            if U(M,k-1)==(3,n):
                continue
        ret=add(ret,o(M,k))
    a,b=v(M,n)
    return SFpsi(a,[],b,[],ret)
def analyze(M):
    if M==[[0,0,0],[1,1,1],[2,1,1],[3,1,1],[2,1,1],[3,1,0],[2,0,0]]:
        return [1,2,6]
    len_=len(M)
    ret=[]
    for i in range(len(M)):
        if M[i][0]==0:
            ret=add(ret,o(M,i))
    return toQ(ret)
def ubi(M):
    if M[-1]==[0,0,0]:
        yield from M[:-1]
    row=max((i for i in [0,1,2] if M[-1][i]))
    br=P(M,row,len(M)-1)
    yield from M[:br]
    for i in range(0,len_):
        for j in range(br,len(M)-1):
            column=M[j][:]
            for k in range(row):
                ubi=j
                while ubi>br:
                    ubi=P(M,k,ubi)
                if ubi==br:
                    column[k]+=i*(M[-1][k]-M[br][k])
            yield column
def unanalyze(s):
    M=[[0,0,0],[1,1,1],[2,1,1],[3,1,1],[2,1,1],[3,1,0],[2,0,0]]
    s=SFQ(s)
    while analyze(M)>s:
        g=ubi(M)
        M=[]
        while analyze(M)<s:
            M.append(next(g))
        if analyze(M)==s:
            return M
def standard(M):
    M2=[[i,i,i] for i in range(len(M)+1)]
    while M2>M:
        g=ubi(M2)
        M2=[]
        while M2<M and len(M2)<len(M):
            M2.append(next(g))
        if M2==M:
            return True
        if M2<M:
            return False
    return False
def add(a,b):
    if a==[]:
        return b
    if b==[]:
        return a
    if [a[0],a[1],a[2]]<[b[0],b[1],b[2]]:
        return b
    return [a[0],a[1],a[2],add(a[3],b)]
def unadd(a,b):
    if a==[]:
        return b
    if b==[]:
        return []
    if [a[0],a[1],a[2]]<[b[0],b[1],b[2]]:
        return b
    if [a[0],a[1],a[2]]>[b[0],b[1],b[2]]:
        return []
    return unadd(a[3],b[3])
def mul(a,b):
    if b==[]:
        return []
    if a==[]:
        return []
    [x,y,z,w]=b
    if [x,y,z,[]]==[[],[],[],[]]:
        return add(a,mul(a,w))
    return add(exp(add(log(a),log(b))),mul(a,w))
def mulQ(a,b):
    return toQ(mul(fromQ(a),fromQ(b)))
def log(a):
    # inverse w^x of first term of a
    if a==[]:
        return []
    [x,y,z,w]=a
    p,q=split(z,[x,add(y,[[],[],[],[]]),[],[]])
    if x==y==p==[]:
        return q
    return [x,y,p,q]
def logQ(a):
    return toQ(log(fromQ(a)))
def exp(a):
    if a<[[],[[],[],[],[]],[],[]]:
        return SF([[],[],a,[]])
    else:
        return SF([a[0],a[1],unadd([a[0],a[1],[],[]],a),[]])
def expQ(a):
    return toQ(exp(fromQ(a)))
def findmaxarg(a,n,b):
    # return the largest nth argument in a, ignoring terms below b
    # and a function that places something at that position,
    #  except the outermost psi, deleting everything afterward
    #  eg psi(W_2+psi_1(W_3)+3)->lambda x:W_2+psi_1(x)
    if a<b or a==[]:
        return [],None
    ret=a[n]
    retf=lambda x:x#lambda x:a[:n]+[x]+[[]]*(3-n)
    # v,f=findmaxarg(a[0],n,b)
    # if v>ret:
    # 	ret=v
    # 	retf=lambda x:f([x,[],[],[]])
    # v,f=findmaxarg(a[1],n,b)
    # if v>ret:
    # 	ret=v
    # 	retf=lambda x:f([a[0],x,[],[]])
    for i in [0,1,2,3]:
        v,f=findmaxarg(a[i],n,b)
        if v>ret:
            ret=v
            retf=lambda x,f=f,i=i:f(a[:i]+[x]+[[]]*(3-i))
    return ret,retf
def findmaxsub(a,b):
    # return the largest subterm in a, ignoring terms below b
    # and a function that places something at that position,
    #  deleting everything afterward
    #  eg psi(W_2+psi_1(W_3)+3)->lambda x:W_2+psi_1(x)
    if a<b or a==[]:
        return [],None
    ret=a
    retf=lambda x:x
    for i in [0,1,2,3]:
        v,f=findmaxsub(a[i],b)
        if v>ret:
            ret=v
            # friggin python closure bullshit
            retf=lambda x,f=f,i=i:a[:i]+[f(x)]+[[]]*(3-i)
    return ret,retf
def split(a,l):
    # split a into terms >=l and terms <l
    if a==[]:
        return [],[]
    [x,y,z,w]=a
    if [x,y,z,[]]<l:
        return [],a
    p,q=split(w,l)
    return [x,y,z,p],q
def SFpsi(a,b,p,c,q):
    # assuming [a,b,c,[]], p, and q are standard,
    # return standard form of [a,add(b,p),add(c,q),[]]
    one=[[],[],[],[]]
    if p==[]:
        if q<[a,b,[],[]]:
            return [a,b,add(c,q),[]]
        [x,y,z,w]=q
        nc=add(c,[x,y,z,[]])
        # m,f=findmaxarg(q,1,[a,[],[],[]])
        # if m>nc:
        # 	raise hell
        # 	t,_=split(m,[x,add(y,one),[],[]])
        # 	print(1,*(toQ(i) for i in [a,b,p,c,q]))
        # 	print(toQ(m),toQ(nc),toQ(t),toQ(f(t)))
        # 	nc=add(t,unadd(f(t),[x,y,z,[]]))
        # m,f=findmaxarg(q,2,[a,b,[],[]])
        # if m>nc:
        # 	t,_=split(m,[x,add(y,one),[],[]])
        # 	print(2,*(toQ(i) for i in [a,b,p,c,q]))
        # 	print(toQ(m),toQ(nc),toQ(t),toQ(f(t)))
        # 	nc=add(t,unadd(f(t),[x,y,z,[]]))
        m,f=findmaxsub([q[0],q[1],q[2],[]],[a,b,[],[]])
        if m>nc:
            t,_=split(m,[x,add(y,one),[],[]])
            nc=add(t,unadd(f(t),[x,y,z,[]]))
        return SFpsi(a,b,p,nc,w)
    # not [a+1,[],[],[]] since stuff like psi_Wfp
    if p<[a,[],[],[]]:
        return SFpsi(a,add(b,p),[],c,q)
    [x,y,z,w]=p
    nb=add(b,[x,y,z,[]])
    # m,f=findmaxarg([x,y,z,[]],1,[a,[],[],[]])
    # if m>nb:
    # 	raise hell
    # 	t,_=split(m,[add(x,one),[],[],[]])
    # 	hrint(3,*(toQ(i) for i in [a,b,p,c,q]))
    # 	hrint(toQ(m),toQ(nb),toQ(t),toQ(f(t)))
    # 	nb=add(t,unadd(f(t),[x,y,z,[]]))
    # # not 100% sure what's up with this
    # m,f=findmaxarg([x,y,z,[]],2,[add(a,[[],[],[],[]]),[],[],[]])
    # if m>nb:
    # 	# wonder if this should be [add(x,one),[],[],[]]
    # 	t,_=split(m,[x,add(y,one),[],[]])
    # 	hrint(4,*(toQ(i) for i in [a,b,p,c,q]))
    # 	hrint(toQ(m),toQ(nb),toQ(t),toQ(f(t)))
    # 	nb=add(t,unadd(f(t),[x,y,z,[]]))
    # still kinda sussy ngl
    m,f=findmaxsub([p[0],p[1],p[2],[]],[add(a,one),[],[],[]])
    if m>nb:
        t,_=split(m,[x,add(y,one),[],[]])
        nb=add(t,unadd(f(t),[x,y,z,[]]))
    return SFpsi(a,nb,w,c,q)
def SF(a):
    if a==[]:
        return []
    [x,y,z,w]=a
    return add(SFpsi(SF(x),[],SF(y),[],SF(z)),SF(w))
def toQ(a,n=1):
    if a==[]:
        return []
    return [n]+toQ(a[0],n+3)+toQ(a[1],n+2)+toQ(a[2],n+1)+toQ(a[3],n)
def fromQ(m):
    s=[(1,[])]
    for i in reversed(m):
        p=[]
        for j in [3,2,1,0]:
            if s[-1][0]<i+j:
                p.append([])
            else:
                p.append(s.pop()[1])
        s.append((i,p))
    return s[-1][1]
def SFQ(a):
    return toQ(SF(fromQ(a)),1)
def c4to3(x):
    if x==[]:
        return x
    return [c4to3(i) for i in x[1:]]
hrint=print
def toexp(m):
    a=analyze(m)
    return tosugar(fromQ(a))
def matfromstr(M):
    m = eval("[" + M.replace(")(", "],[").replace("(", "[").replace(")", "]") + "]")
    for i in range(len(m)):
        while len(m[i])<3:
            m[i].append(0)
    return m
print('Only works for matrices smaller than (0)(1,1,1)(2,1,1)(3,1,1)(2,1,1)(3,1,0)(2,0,0)')
while True:
    M=input('BMS matrix> ')
    k=0
    m=eval("["+M.replace(")(","],[").replace("(","[").replace(")","]")+"]")
    len_=len(m)
    for i in range(len(m)):
        if k<len(m[i]):
            k=len(m[i])
        while len(m[i])<3:
            m[i].append(0)
    if k<4:
        print(f'{"Non-"*(not standard(m))}{chr(115-standard(m)*32)}tandard')
    if not standard(m) and k<4:
        print(f'Standardized: {str(unanalyze(analyze(m)))[1:-1].replace("], [",")(").replace("[","(").replace("]",")").replace(" ","")}')
    if unanalyze(analyze(m))>=[[0,0,0],[1,1,1],[2,1,1],[3,1,1],[1,1,1],[2,1,1],[3,1,0],[4,2,1],[5,2,1],[6,2,1],[4,2,1],[5,2,1],[6,2,0],[7,3,1],[8,3,1],[9,3,1]]:
        print('Probably wrong')
    print(f'? sequence: {f"{analyze(m)}".replace("[","(").replace("]",")")}')
    print(f'solarzone\'s notation: {tosolarzone(fromQ(analyze(m)))}')
    if k<4:
        print(f'Expr: {toexp(m)}')
    print()