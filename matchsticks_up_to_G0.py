from ordinals_up_to_G0 import *
from PIL import Image, ImageDraw
width=2000
size=(width,width*9//16)
im=Image.new(mode='RGB',size=size)
k=size[1]//2
draw = ImageDraw.Draw(im)
def get_terms(x):
    if x<w:
        return [x]*(x!=0)
    else:
        return [Ordinal(x.subscript,x.arg)]*x.copies+get_terms(x.addend)
def sub1(ord):
    if isinstance(ord,int):
        if ord!=0:
            return ord-1
        else:
            raise Exception("0-1 is -1, which is not an ordinal")
    else:
        if ord.is_successor():
            return Ordinal(ord.subscript,ord.arg,ord.copies,sub1(ord.addend))
        raise Exception('Not defined for limit ordinals')
def fs(ord,x):
    if ord.copies==1 and ord.addend==0:
        k=ord.veblen()
        if k[0]==0 and is_successor(k[1]):
            return (w**(sub1(k[1])))*x
        if x==0 and k[1]==0 and is_successor(k[0]):
            return 0
        if k[1] == 0 and is_successor(k[0]):
            return phi(sub1(k[0]),fs(phi(k[0],0),x-1))
        if x==0 and is_successor(k[0]) and is_successor(k[1]):
            return phi(k[0],sub1(k[1]))+1
        if is_successor(k[0]) and is_successor(k[1]):
            return phi(sub1(k[0]),fs(phi(k[0],k[1]),x-1))
        if is_limit(k[0]) and k[1]==0:
            return phi(fs(k[0],x),0)
        if is_limit(k[1]):
            return phi(k[0],fs(k[1],x))
        if is_successor(k[1]) and is_limit(k[0]):
            return phi(fs(k[0],x),phi(k[0],sub1(k[1]))+1)
    else:
        return sum(get_terms(ord)[:-1])+fs(get_terms(ord)[-1],x)
def nocopies(x):
    if type(x)==Ordinal:
        return Ordinal(x.subscript,x.arg)
    return 1
def matchsticks_text(ord):
    if ord==1:
        return '|'
    if ord.copies == 1 and ord.addend == 0:
        if ord==w:
            return 'w'
        else:
            return f'({" ".join([matchsticks_text(nocopies(fs(ord,i))) for i in range(1,5)])})...'
def matchsticks_img(ord,ht,lx,rx,l=0,r=0,labels=True,p=0):
    global k
    #print(ht, lx, rx, ord)
    if l==0 and r==0:
        draw.text((width//2,1),f'The ordinal '+str(ord).replace('ω','w').replace('ε','e').replace('ζ','z').replace('η','n').replace('φ','p'),anchor='rt')
    if type(ord)==int:
        for i in range(1,ord+1):
            draw.line(((round(lx+((2**(i-1)-1)/(2**(i-1)))*(rx-lx)), round(k - (ht/(2**(i-1))))), (round(lx+((2**(i-1)-1)/(2**(i-1)))*(rx-lx)), round(k + (ht/(2**(i-1)))))))
            if i == 1 and r != 0 and labels:
                s = str(r + 1).replace('ω','w').replace('ε','e').replace('ζ','z').replace('η','n').replace('φ','p')
                draw.text((round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx)) - len(s) * 6 * (i != 1),k + (round(ht / (2 ** (i - 1)))) * ((-1) ** i) - (10 * (i % 2 == 1))), s,fill='#ff0000')
    else:
        if ord.copies == 1 and ord.addend == 0:
            i=1
            while round(lx+((2**(i)-1)/(2**(i)))*(rx-lx))-round(lx+((2**(i-1)-1)/(2**(i-1)))*(rx-lx))>0:
                matchsticks_img(nocopies(fs(ord,i)),round(ht/(2**(i-1))),round(lx+((2**(i-1)-1)/(2**(i-1)))*(rx-lx)),round(lx+((2**(i)-1)/(2**(i)))*(rx-lx)),l+1, labels=labels)
                if l==0 and round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx))<round(width*.95) and round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx))<round(rx*.95) and labels:
                    if i!=1:
                        s=str(r+fs(ord,i-1)).replace('ω','w').replace('ε','e').replace('ζ','z').replace('η','n').replace('φ','p')
                    else:
                        s=str(r).replace('ω','w').replace('ε','e').replace('ζ','z').replace('η','n').replace('φ','p')
                    draw.text((round(lx + ((2 ** (i - 1) - 1) / (2 ** (i - 1))) * (rx - lx))-len(s)*6*(i!=1), k+(round(ht / (2 ** (i - 1))))*((-1)**i)-(10*(i%2==1))),s,fill='#ff0000')
                i+=1
            if l==0 and labels and p==0:
                s = str(r + ord).replace('ω','w').replace('ε','e').replace('ζ','z').replace('η','n').replace('φ','p')
                if l == 0: draw.text((rx - len(s) * 6, k - 20), s,fill='#ff0000')
        else:
            for i in range(len(get_terms(ord))):
                matchsticks_img(get_terms(ord)[i], ht / (2 ** (i)),round(lx + ((2 ** (i) - 1) / (2 ** (i))) * (rx - lx)),round(lx + ((2 ** (i + 1) - 1) / (2 ** (i + 1))) * (rx - lx)), 0,sum(get_terms(ord)[:i]), labels=labels, p=1)

def get_image(M,w_=1000,l=True):
    global width
    global size
    global k
    global im
    global draw
    width = w_
    size = (width, width * 3 // 4)
    k = size[1] // 2
    im = Image.new(mode='RGB', size=size)
    draw = ImageDraw.Draw(im)
    matchsticks_img(M,k-20,20,width-20,labels=l)
    im.save('matchsticks.png')
