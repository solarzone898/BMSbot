from PIL import Image, ImageDraw
width=1000
size = (width, width * 9 // 16)
k = size[1] // 2
im = Image.new(mode='RGB', size=size)
draw = ImageDraw.Draw(im)
def P(M,r,n):
    if r==-1:
        return n-1
    else:
        ret=P(M,r-1,n)
        while ret>-1 and M[ret][r]>=M[n][r]:
            ret=P(M,r-1,ret)
        return ret
def ubi(M,n):
    if M[-1]==[0,0,0]:
        yield from M[:-1]
    row=max((i for i in range(len(M[0])) if M[-1][i]))
    br=P(M,row,len(M)-1)
    yield from M[:br]
    for i in range(0,n):
        for j in range(br,len(M)-1):
            column=M[j][:]
            for k in range(row):
                ubi=j
                while ubi>br:
                    ubi=P(M,k,ubi)
                if ubi==br:
                    column[k]+=i*(M[-1][k]-M[br][k])
            yield column
def fs(M,n):
    return list(ubi(M,n))
def isnat(M):
    for i in M:
        k=0
        for j in i:
            if j!=0: k=1
        if k:
            return False
    return True
def matfromstr(M):
    m = eval("[" + M.replace(")(", "],[").replace("(", "[").replace(")", "]") + "]")
    if m!=[]:
        k=max([len(i) for i in m])
    else:
        k=0
    for i in range(len(m)):
        while len(m[i])<k:
            m[i].append(0)
    return m
def nocopies(M):
    if not isnat(M):
        x=[]
        for i in range(len(M)):
            k=1
            for j in M[i]:
                if j != 0: k = 0
            if k and i!=0:
                break
            x+=[M[i]]
        return x
    if M!=[]:
        return [M[0]]
    return []
def Sum(x):
    a=[]
    for i in x:
        a+=i
    return a
def terms(M):
    x=[]
    for i in M:
        k=1
        for j in i:
            if j!=0: k=0
        if k:
            x.append([[0]*len(i)])
        else:
            x[-1].append(i)
    return x
def isempty(M):
    k=1
    for j in M:
        if j != 0: k = 0
    return k
def matchsticks(M,ht,lx,rx,l=0,r=[],labels=True):
    global k
    if l == 0:
        draw.text((width//2, 10), f'The ordinal {str(M)[1:-1].replace("], [",")(").replace("[","(").replace("]",")").replace(" ","")}',anchor='ma')
    if isnat(M):
        for i in range(1, len(M)+ 1):
            draw.line(((round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx)),round(k - (ht / (2 ** (i - 1))))), (round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx)),round(k + (ht / (2 ** (i - 1)))))))
            if i==1 and r!=[] and labels:
                s = str(r + [[0]])[1:-1].replace("], [", ")(").replace("[", "(").replace("]", ")").replace(" ", "")
                draw.text((round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx)) - len(s) * 6 * (i != 1),k + (round(ht / (2 ** (i - 1)))) * ((-1) ** i) - (10 * (i % 2 == 1))), s)
    else:
        if len(terms(M))==1:
            i = 1
            while round(lx + ((2 ** (i) - 1) / (2 ** (i))) * (rx - lx)) - round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx)) > 0:
                matchsticks(nocopies(fs(M, i)), round(ht / (2 ** (i - 1))),round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx)),round(lx + ((2 ** (i) - 1) / (2 ** (i))) * (rx - lx)), l + 1, labels=labels)
                if l==0 and round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx))<round(width*.95) and round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx))<round(rx*.95) and labels:
                    s=str(r+list(ubi(M,i-1+(r!=[]))))[1:-1].replace("], [", ")(").replace("[", "(").replace("]", ")").replace(" ", "")
                    draw.text((round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx))-len(s)*6*(i!=1), k+(round(ht / (2 ** (i - 1))))*((-1)**i)-(10*(i%2==1))),s)
                i += 1
                s = str(r + M)[1:-1].replace("], [", ")(").replace("[", "(").replace("]", ")").replace(" ", "")
                if l==0 and labels: draw.text((rx-len(s)*6, k-20),s)
        else:
            z=terms(M)
            m=0
            while isnat(z[-1]):
                z=z[:-1]
                m+=1
            z=z+[[[0]]*m]
            for i in range(len(z)):
                matchsticks(z[i], ht / (2 ** (i)), round(lx + ((2 ** (i) - 1) / (2 ** (i))) * (rx - lx)),round(lx + ((2 ** (i + 1) - 1) / (2 ** (i + 1))) * (rx - lx)), 0, Sum(z[:i]), labels=labels)

global width
global size
global k
global im
global draw
width = w
size = (width, width * 3 // 4)
while True:
    k = size[1] // 2
    im = Image.new(mode='RGB', size=size)
    draw = ImageDraw.Draw(im)
    matchsticks(matfromstr(input('> ')),k-20,20,width-20,labels=l)
    im.save('matchsticks.png')
