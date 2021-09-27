class Encryptor:
    #copyright Sphephelo Mabena
    #all rights reserved
    e0="egsxgec$r"
    e1="mjsvx$$$r"
    e2="#d4%78vxr"
    e3="#3#3#3#3r"
    e4="@[@[@[@[r"
    e5="gcpmgmoor"
    e6="btbtbtbtr"
    e7="vbs#d:ucr"
    e8="mythzllor"
    e9="8043gdx#r"
    edash="hfxv55$7r"
    eHash="bvcr##r"
    ea="zx48ed2dr"
    eb="jn9u4fqxr"
    ec="vbn877zxr"
    ed="w98xjh3?r"
    ee="#mxhkndtr"
    ef="9dnj9d%kr"
    eg="ikzh@!0$r"
    eh="ut^hs$jxr"
    ei="?mx>}+8fr"
    ej="*w#&^@9qr"
    ek="k.fe@$xwr"
    el="hhmso#9@r"
    em="*bv<t^&7r"
    en="mnwq&j)nr"
    eo="nU9%?@khr"
    ep="#vb&jhobr"
    #copyright Sphephelo Mabena
    #all rights reserved
    eq="bhc@4:jir"
    er="#bjg@e&#r"
    es="#bcgxs%tr"
    et="&vhx4mnjr"
    eu="lcflcflhr"
    ev="zvchuebpr"
    ew="xcexeubzr"
    ex="xz#hblhor"
    ey="#jdbx#j8r"
    ez="$hf%#@88r"
    whitenode="a#r"
    a="a"
    b="b"
    c="c"
    d="d"
    e="e"
    f="f"
    g="g"
    h="h"
    i="i"
    j="j"
    k="k"
    l="l"
    m="m"
    n="n"
    o="o"
    p="p"
    q="q"
    r="r"
    s="s"
    t="t"
    u="u"
    v="v"
    w="w"
    xx="x"
    y="y"
    z="z"
    #copyright Sphephelo Mabena
    #all rights reserved
    ta=ea.split("r")[0]#test a
    tb=eb.split("r")[0]
    tc=ec.split("r")[0]
    td=ed.split("r")[0]
    te=ee.split("r")[0]
    tf=ef.split("r")[0]
    tg=eg.split("r")[0]
    th=eh.split("r")[0]
    ti=ei.split("r")[0]
    tj=ej.split("r")[0]
    tk=ek.split("r")[0]
    tl=el.split("r")[0]
    tm=em.split("r")[0]
    tn=en.split("r")[0]
    to=eo.split("r")[0]
    tp=ep.split("r")[0]
    tq=eq.split("r")[0]
    ts=es.split("r")[0]
    tt=et.split("r")[0]
    tr=er.split("r")[0]
    tu=eu.split("r")[0]
    tv=ev.split("r")[0]
    tw=ew.split("r")[0]
    tx=ex.split("r")[0]
    ty=ey.split("r")[0]
    tz=ez.split("r")[0]
    twhite=whitenode.split("r")[0]
    t1=e1.split("r")[0]
    t2=e2.split("r")[0]
    t3=e3.split("r")[0]
    t4=e4.split("r")[0]
    t5=e5.split("r")[0]
    t6=e6.split("r")[0]
    t7=e7.split("r")[0]
    t8=e8.split("r")[0]
    t9=e9.split("r")[0]
    t0=e0.split("r")[0]
    tHash=eHash.split("r")[0]
    #copyright Sphephelo Mabena
    #all rights reserved
    

    def Encryption(self,word):
        
        text=list(word)
        x=0
        letter=text
		#copyright Sphephelo Mabena
        #all rights reserved
	    
        encrypted=""
		
        while x<len(text):
        
            if letter[x] == " ":
                text[x]=self.whitenode
                
			
            if letter[x] =="0":
                text[x]=self.e0
                
            
            if letter[x] == "1":
                text[x]=self.e1
                

            if letter[x] == "2":
                text[x]=self.e2
                x=x+1
        
            if letter[x] == "3":
                text[x]=self.e3
                
            
            if letter[x] == "4":
                text[x]=self.e4
                
            
            if letter[x] == "5":
                text[x]=self.e5
                x=x+1
            
            if letter[x] == "6":
                text[x]=self.e6
            
        
            if letter[x] == "7":
                text[x]=self.e7
                
            
            if letter[x] == "8":
                text[x]=self.e8
                
            
            if letter[x]=="9":
                text[x]=self.e9
                
            
            if letter[x] == "#":
                text[x]=self.eHash
                
                
        
            if letter[x] == "a":
                text[x]=self.ea
                
            
            if letter[x] =="b":
                text[x]=self.eb
                
            
            if letter[x] =="c":
                text[x]=self.ec
                
            
            if letter[x]=="d":
                text[x]=self.ed
                
            
            if letter[x]=="e":
                text[x]=self.ee
                
            
            if letter[x]=="f":
                text[x]=self.ef
                
            
            if letter[x]== "g":
                text[x]=self.eg
                
            
            if letter[x]== "h":
                text[x]=self.eh
            
            #copyright Sphephelo Mabena
            #all rights reserved    
            
            if letter[x] == "i":
                text[x]=self.ei
                
        
            if letter[x] == "j":
                text[x]=self.ej
                
        
            if letter[x] == "k":
                text[x]=self.ek
            

            if letter[x] ==  "l":
                text[x]=self.el

            if letter[x] == "n":
                text[x]=self.en
                
            
            if letter[x]== "o":
                text[x]=self.eo
                
            
            if letter[x] == "p":
                text[x]=self.ep
            
            
            if letter[x] == "q":
                text[x]=self.eq
            

            if letter[x] == "r":
                text[x]=self.er
                
            
            if letter[x] == "s":
                text[x]=self.es
                
            
            if letter[x] == "t":
                text[x]=self.et
                
            
            if letter[x] == "u":
                text[x]=self.eu
            
            
            if letter[x] == "v":
                text[x]=self.ev
                
            
            if letter[x] ==  "w":
                text[x]=self.ew
                
            
            if letter[x] == "x":
                text[x]=self.ex
            
            
            if letter[x] == "y":
                text[x]=self.ey
                
            
            if letter[x] == "z":
                text[x]=self.ez
                
		
            encrypted +=text[x]
            x +=1
        return encrypted
    def Decrypt(self,etext):
        text=etext.split("r")
        decrypted=""
        #copyright Sphephelo Mabena
         #all rights reserved
        y=0

        while y<len(text):
            ref=text[y]
            if self.ta == ref:
                ref=self.a
            
            if self.twhite == ref:
            
                ref=" "
            
            if self.tHash == ref:
            
                ref="#"
            
            if self.t0 == ref:
            
                ref="0"
            
            if self.t1 == ref:
            
                ref="1"
            
            if self.t2 == ref:
            
                ref="2"
            
            if self.t3 ==ref:
            
                ref="3"
            
            if self.t4 == ref:
            
                ref="4"
            
            if self.t5 == ref:
            
                ref="5"
            
            if self.t6 == ref:
            
                ref="6"
            
            if self.t7 == ref:
            
                ref="7"
            
            if self.t8 == ref:
            
                ref="8"
            
            if self.t9 == ref:
            
                ref="9"
            
            if self.tb == ref:
            
                ref=self.b
            
            if self.tc == ref:
            
                ref=self.c
            
            if self.td == ref:
            
                ref=self.d

            if self.te == ref:
            
                ref=self.e
            
            if self.tg == ref:
            
                ref=self.f
            
            if self.tg == ref:
            
                ref=self.g
            
            if self.th == ref:
            
                ref=self.h
            
            if self.ti == ref:
            
                ref=self.i
            
            if self.tj == ref:
            
                ref=self.j
            
            if self.tk == ref:
            
                ref=self.k
            
            if self.tl == ref:
            
                ref=self.l
            
            if self.tm == ref:
            
                ref=self.m
            
            if self.tn == ref:
            
                ref=self.n
            
            if self.to == ref:
            
                ref=self.o
            
            if self.tp == ref:
            
                ref=self.p
            
            if self.t5 == ref:
            
                ref=self.q
            
            if self.tr == ref:
            
                ref=self.r
            #copyright Sphephelo Mabena
         #all rights reserved
            if self.ts == ref:
            
                ref=self.s
            
            if self.tt == ref:
            
                ref=self.t
            
            if self.tu == ref:
            
                ref=self.u
            
            if self.tv == ref:
            
                ref=self.v
            
            if self.tw == ref:
            
                ref=self.w
        
            if self.tx == ref:
            
                ref=self.xx
            
            if self.ty == ref:
            
                ref=self.y
            
            if self.tz == ref:
            
                ref=self.z
            
            decrypted +=ref
            y +=1

        return decrypted

					
    


encrypt = Encryptor()


#print(testword)


#copyright Sphephelo Mabena
    #all rights reserved




    
