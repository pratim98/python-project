from tkinter import *
import math
import pyttsx3
engine = pyttsx3.init()

expression = "" 
object = Tk()
 
def enter(num): 
    global expression 
    expression = expression + str(num)
    fieldd.set(expression)
    engine.say(expression)
    engine.runAndWait()


    
def sin():
  try: 
    global expression
    n=float(expression)

    sinval = math.sin(n);
    val=round(sinval)
    fieldd.set(val)
    expression=str(val)


  except:
        fieldd.set(" error ") 
        expression = ""
def pie():
  try: 
    global expression
    if(expression!=""):
        n=float(expression)
        pieval=n*math.pi
        fieldd.set(pieval)
        expression=str(pieval)
        


    else:
        pieval=math.pi
        fieldd.set(pieval)
        expression=str(pieval)
        

  except:
        fieldd.set(" error ") 
        expression = ""  
def cos():
  try: 
    global expression
    n=float(expression)

    cosval = math.cos(n);
    val=round(cosval)
    fieldd.set(val)
    expression=str(val)
    

  except:
        fieldd.set(" error ") 
        expression = ""
def exp():
  try: 
    global expression
    if(expression!=""):
        n=float(expression)
        expval=math.exp(n);
        fieldd.set(expval)
        expression=str(expval)


    else:
       expval = math.exp(1);
       val=expval
       fieldd.set(val)
       expression=str(val)
       

  except:
        fieldd.set(" error ") 
        expression = ""        
        
def tan():
  try: 
    global expression
    n=float(expression)

    tanval = math.tan(n);
    val=tanval
    fieldd.set(val)
    expression=str(val)
    

  except:
        fieldd.set(" error ") 
        expression = ""
def log():
  try: 
    global expression
    n=float(expression)

    logval = math.log10(n);
    val=logval
    fieldd.set(val)
    expression=str(val)
    

  except:
        fieldd.set(" error ") 
        expression = ""

def fact():
    try:
      global expression
      expression = str(eval(expression))
      n = int(expression)
      f = 1
  
      for i in range(1,n+1): 
       f = f * i  
      fieldd.set(f)
      expression=str(f)
      engine.say(expression)
      engine.runAndWait()


     

    except:
        fieldd.set(" error ") 
        expression = "" 

        
def cl():
 try:   
  global expression
  a=str(expression)
  t=len(a)
  l=a[t-1]
  b=a[:-1]
  fieldd.set(b)
  expression=str(b)
 except:
     fieldd.set(0)
     expression=""



    
def sqr():
   try:
    global expression
    total=int(expression)*int(expression)
    fieldd.set(total)
    expression=str(total)
    engine.say(total)
    engine.runAndWait()




   except:
        fieldd.set(" error ") 
        expression = "" 
def per():
   try:
    global expression
    total=float(expression)/100
    fieldd.set(total)
    expression=str(total)
    engine.say(total)
    engine.runAndWait()



   except:
        fieldd.set(" error ") 
        expression = ""
    
def sqrtt(): 
   try:
    global expression
    total=math.sqrt(int(expression))
    fieldd.set(total)
    expression=str(total)
    engine.say(total)
    engine.runAndWait()


   except: 
  
        fieldd.set(" error ") 
        expression = "" 
def equal(): 

    try: 
  
        global expression 
        total = str(eval(expression))
        fieldd.set(total) 
        expression =total
        s=str(expression)

        engine.say("equals to"+s)
        engine.runAndWait()



    except: 
  
        fieldd.set(" error ") 
        expression = "" 
  

def clear(): 
    global expression 
    expression = "" 
    fieldd.set("")

  
def closee():
    object.destroy()
menu=Menu(object)
filemenue=Menu(menu,tearoff=False)

menu.add_cascade(label="Close",command=closee)
object.config(menu=menu)


   
object.configure(background="light grey") 
  
   
object.title("voice Calculator") 
  
    
object.geometry("273x345") 
  

fieldd= StringVar() 
  

expression_field= Entry(object, textvariable=fieldd,font=('arial',15,'bold'),bg="powder blue",bd=9,width=15,justify="right") 

expression_field.grid(columnspan=5, ipadx=42) 


fieldd.set('INPUT') 
  
button9 = Button(object, text=' 9 ',command=lambda: enter(9), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3)
button9.grid(row=5,column=0)

button8 = Button(object, text=' 8 ',command=lambda: enter(8), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button8.grid(row=5, column=1)

button7 = Button(object, text=' 7 ',command=lambda: enter(7), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3)
button7.grid(row=5, column=2)

button6 = Button(object, text=' 6 ',command=lambda: enter(6), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button6.grid(row=6, column=0)

button5 = Button(object, text=' 5 ',command=lambda: enter(5), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button5.grid(row=6, column=1)

button4 = Button(object, text=' 4 ',command=lambda: enter(4), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button4.grid(row=6, column=2)

button3 = Button(object, text=' 3 ',command=lambda: enter(3), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3)
button3.grid(row=7, column=0)

button2 = Button(object, text=' 2 ',command=lambda: enter(2), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button2.grid(row=7, column=1)

button1 = Button(object, text=' 1 ',command=lambda: enter(1), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button1.grid(row=7, column=2)

button0 = Button(object, text=' 0 ',command=lambda: enter(0), height=2, width=8,font=('arial',9,'bold'),bg="powder blue",bd=3) 
button0.grid(row=8, column=1)

per = Button(object, text=' % ',font=('arial',9),command=per, height=2, width=8,bd=3)
per.grid(row=8, column=2)

buttondot=Button(object, text=' . ',font=('arial',9),command=lambda: enter("."), height=2, width=8,bd=3) 
buttondot.grid(row=8, column=0)

plus = Button(object, text=' ✚ ',font=('arial',9),command=lambda: enter("+"), height=2, width=8,bd=3) 
plus.grid(row=3, column=3)

minus = Button(object, text=' ➖ ',font=('arial',9),command=lambda: enter("-"), height=2, width=8,bd=3)
minus.grid(row=4, column=3)

multiply = Button(object, text=' ✕ ',font=('arial',9),command=lambda: enter("*"), height=2, width=8,bd=3)
multiply.grid(row=5, column=3)

divide = Button(object, text=' ➗ ',font=('arial',9), command=lambda: enter("/"), height=2, width=8,bd=3)
divide.grid(row=6, column=3)

equal = Button(object, text=' = ',command=equal, height=2, width=8,bd=3) 
equal.grid(row=8, column=3)

clear = Button(object, text='C',font=('arial',9),command=clear, height=2, width=8,bd=3) 
clear.grid(row=2, column=2)

sqrtt = Button(object, text='√ ',font=('arial',9),command=sqrtt,height=2, width=8,bd=3) 
sqrtt.grid(row=2, column=0)

sqr = Button(object, text=' x²',font=('arial',9),command=sqr,height=2, width=8,bd=3) 
sqr.grid(row=2, column=1)

sin = Button(object, text=' sin',font=('arial',9),command=sin,height=2, width=8,bd=3) 
sin.grid(row=3, column=1)

cos = Button(object, text=' cos',font=('arial',9),command=cos,height=2, width=8,bd=3) 
cos.grid(row=3, column=2)

fact = Button(object, text='!',font=('arial',9),command=fact,height=2, width=8,bd=3) 
fact.grid(row=7, column=3)

tan = Button(object, text=' tan',font=('arial',9),command=tan,height=2, width=8,bd=3) 
tan.grid(row=3, column=0)

log = Button(object, text=' log',font=('arial',9),command=log,height=2, width=8,bd=3) 
log.grid(row=4, column=0)

pie = Button(object, text='π',font=('arial',9),command=pie, height=2, width=8,bd=3) 
pie.grid(row=4, column=1)

exp = Button(object, text=' e^x',font=('arial',9),command=exp,height=2, width=8,bd=3) 
exp.grid(row=4, column=2)

cl= Button(object, text='❎',font=('arial',9),command=cl,height=2, width=8,bd=3) 
cl.grid(row=2, column=3)
    
