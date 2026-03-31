from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import load,dump





def play():
    n=w.n.text()
    if not(n.isdecimal() and(int(n)>0)):
        QMessageBox.critical(w,"Error","Please enter a positive number")
    else:
        strecture(int(n),f1)
        result(f1)







def strecture(n,f1):
    f1=open(f1,"wb")
    e={"cycle":"","binary":"","hexadecimal":"","period":0}
    test=True
    z=n
    ch=""
    ch1=""
    ch2=""
    p=0
    while test:
        ch+=str(n)+"#"
        b=base_2(n)
        b=b[::-1]
        ch2+=b+"#"
        x=base_10(b)
        x+=2
        y=hexadecimal(n,16)
        ch1+=y+"#"
        if x==z:
            test=False
            ch+=str(x)+"#"
            n=x
            y=hexadecimal(n,16)
            ch1+=y+"#"
            b=base_2(n)
            b=b[::-1]
            ch2+=b+"#"
            p+=1
        else:
            n=x
            p+=1
        if p>1024:
            QMessageBox.critical(w,"Error","Sorry this number is going to infinity")
            break
    e["cycle"]=ch
    e["period"]=p
    e["hexadecimal"]=ch1
    e["binary"]=ch2
    dump(e,f1)
    f1.close()
    
    
    
    
    
def base_2(n):
    if n == 0:
        return "0"
    ch = ""
    while n != 0:
        r = n % 2
        ch = str(r) + ch
        n = n // 2
    return ch





def base_10(b):
    d=0
    p=1
    for i in range(len(b)-1,-1,-1):
        d=d+int(b[i])*p
        p=p*2
    return d






def hexadecimal(x,b):
    ch=""
    while x!=0:
        r=x%b
        x=x//b
        if r<10:
            ch=str(r)+ch
        else:
            ch=chr(r+55)+ch
    return ch





def result (f1):
    f1=open(f1,"rb")
    i=0
    ok=True
    while ok:
        try:
            e=load(f1)  
            w.tab.insertRow(i)
            w.tab.setItem(i,0,QTableWidgetItem(e["cycle"]))
            w.tab.setItem(i,1,QTableWidgetItem(e["binary"]))
            w.tab.setItem(i,2,QTableWidgetItem(e["hexadecimal"]))
            w.tab.setItem(i,3,QTableWidgetItem(str(e["period"])))
            i+=1
        except:
            ok=False
    f1.close()
    
    
    
    
    
f1="amplitude.dat"       
app=QApplication([])
w=loadUi("interface_project.ui")
w.show()
w.b1.clicked.connect(play)
app.exec_()
