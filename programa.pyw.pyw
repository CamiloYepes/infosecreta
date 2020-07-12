from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os.path

#-----------------------------------------ventana0-----------------------------------
def ventana0():
    ventana0=tk.Tk()
    ventana0.title('Tic Tac Toe')
    ventana0.iconbitmap('tres-raya.ico')            #creación ventana con imagen superior
    ventana0.config(bg='black')

    frame=Frame(ventana0)
    frame.config(bg='black')                        #creación ventana con objetos(botones,texto,etc)
    frame.pack(pady=30,padx=100)


    imagen=tk.PhotoImage(file='Tic Tac Toe.png')
    imagen=imagen.subsample(2,2)
    label=tk.Label(frame,image=imagen)              #imagenes
    label.place(x=0,y=250)
    label.grid(row=0,column=0,columnspan=2)

    texto0=tk.Label(frame,text='')
    texto0.config(bg='black')
    texto0.grid(row=1,column=0,)

    texto1=tk.Label(frame,text='jugador 1')
    texto1.config(bg='black',fg='white')            #textos
    texto1.grid(row=2,column=0,pady=10)

    jugador1=tk.Entry(frame)
    jugador1.config(justify='center')               #entrada texto
    jugador1.grid(row=2,column=1)
    
    def jugar():
        a=jugador1.get()
        if a=='0000':
            ventana0.destroy()                      #función botones
            ventana2()
        else:
            ventana0.destroy()
            juego()
        
    boton_j=Button(frame,text='jugar', command=jugar)
    boton_j.grid(row=4,column=0, columnspan=2,ipadx=85)     #botones

    mainloop()
#-----------------------------------------ventana1---------------------------------------
    
def juego():
    v_juego=tk.Tk()
    v_juego.title('Tic Tac Toe')
    v_juego.iconbitmap('tres-raya.ico')
    v_juego.config(bg='black')

    frame=Frame(v_juego)
    frame.config(bg='white')                        #creación ventana con objetos(botones,texto,etc)
    frame.pack(pady=30,padx=100)

    imagen11=tk.PhotoImage(file='cuadrado.gif')
    imagen11=imagen11.subsample(1,1)
    label=tk.Label(frame,image=imagen11)
    label.grid(row=1,column=2)

    imagen12=tk.PhotoImage(file='cuadrado.gif')
    imagen12=imagen12.subsample(1,1)
    label=tk.Label(frame,image=imagen12)
    label.grid(row=1,column=3)

    imagen13=tk.PhotoImage(file='circulo.gif')
    imagen13=imagen13.subsample(1,1)
    label=tk.Label(frame,image=imagen13)
    label.grid(row=1,column=4)

    imagen21=tk.PhotoImage(file='circulo.gif')
    imagen21=imagen21.subsample(1,1)
    label=tk.Label(frame,image=imagen21)
    label.grid(row=2,column=2)

    imagen22=tk.PhotoImage(file='cuadrado.gif')
    imagen22=imagen22.subsample(1,1)
    label=tk.Label(frame,image=imagen22)
    label.grid(row=2,column=3)

    imagen23=tk.PhotoImage(file='circulo.gif')
    imagen23=imagen23.subsample(1,1)
    label=tk.Label(frame,image=imagen23)
    label.grid(row=2,column=4)

    imagen31=tk.PhotoImage(file='cuadrado.gif')
    imagen31=imagen31.subsample(1,1)
    label=tk.Label(frame,image=imagen31)
    label.grid(row=3,column=2)

    imagen32=tk.PhotoImage(file='circulo.gif')
    imagen32=imagen32.subsample(1,1)
    label=tk.Label(frame,image=imagen32)
    label.grid(row=3,column=3)

    imagen33=tk.PhotoImage(file='cuadrado.gif')
    imagen33=imagen33.subsample(1,1)
    label=tk.Label(frame,image=imagen33)
    label.grid(row=3,column=4)
        
    numero1=tk.Label(frame,text='1')
    numero1.config(bg='black',fg='white',font=10)            #textos
    numero1.grid(row=1,column=1,ipady=50)
        
    numero2=tk.Label(frame,text='2')
    numero2.config(bg='black',fg='white',font=10)            #textos
    numero2.grid(row=2,column=1,ipady=50)
        
    numero3=tk.Label(frame,text='3')
    numero3.config(bg='black',fg='white',font=10)            #textos
    numero3.grid(row=3,column=1,ipady=50)

    tcoordenada=tk.Label(frame,text='A')
    tcoordenada.config(bg='black',fg='white',font=10)            #textos
    tcoordenada.grid(row=0,column=2,ipadx=57)
        
    tcoordenada=tk.Label(frame,text='B')
    tcoordenada.config(bg='black',fg='white',font=10)            #textos
    tcoordenada.grid(row=0,column=3,ipadx=57)
        
    tcoordenada=tk.Label(frame,text='C')
    tcoordenada.config(bg='black',fg='white',font=10)            #textos
    tcoordenada.grid(row=0,column=4,ipadx=57)

    basio=tk.Label(frame,text='')
    basio.config(bg='black')            #textos
    basio.grid(row=0,column=1,ipady=4,ipadx=6)

    tcoordenada=tk.Label(frame,text='coordenada')
    tcoordenada.config(bg='black',fg='white',font=10)            #textos
    tcoordenada.grid(row=4,column=1,columnspan=2,ipady=10,ipadx=20)

    coordenada=tk.Entry(frame)
    coordenada.config(justify='center')               #entrada texto
    coordenada.grid(row=4,column=3,columnspan=4,ipadx=70,ipady=15)

    mainloop()

#----------------------------------------ventana2----------------------------------------
def ventana2():
    ventana2=tk.Tk()
    ventana2.title('Tic Tac Toe')
    ventana2.iconbitmap('tres-raya.ico')
    ventana2.config(bg='black')

    frame=Frame(ventana2)
    frame.config(bg='black')
    frame.pack(pady=100,padx=100)

    def ini():
        ventana2.destroy()
        ventana21()

    boton_i=tk.Button(frame,text='iniciar sesión',command=ini)
    boton_i.config(bg='black',fg='white',font=(20))
    boton_i.pack(ipady=5,ipadx=20,fill=tk.X)

    def reg():
        ventana2.destroy()
        ventana22()

    boton_r=tk.Button(frame,text='registrarse',command=reg)
    boton_r.config(bg='black',fg='white',font=(20))
    boton_r.pack(ipady=5,ipadx=20,fill=tk.X)

    def salir():
        ventana2.destroy()
        
    boton_s=tk.Button(frame,text='salir', command=salir)
    boton_s.config(bg='black',fg='white',font=(20))
    boton_s.pack(ipady=5,ipadx=20,fill=tk.X)
    
    mainloop()
    
#------------------------------------------ventana21------------------------------------------
def ventana21():
    ventana21=tk.Tk()
    ventana21.title('Tic Tac Toe')
    ventana21.iconbitmap('tres-raya.ico')
    ventana21.config(bg='black')

    frame=Frame(ventana21)
    frame.config(bg='black')
    frame.pack(pady=30,padx=100)

    texto1=tk.Label(frame,text='Usuario')
    texto1.config(bg='black',fg='white')
    texto1.grid(row=0,column=0,pady=10)

    usuario=tk.Entry(frame)
    usuario.config(justify='center')
    usuario.grid(row=0,column=1)

    texto2=tk.Label(frame,text='Contraseña')
    texto2.config(bg='black',fg='white')
    texto2.grid(row=1,column=0,pady=10)

    contraseña=tk.Entry(frame)
    contraseña.config(justify='center',show='*')
    contraseña.grid(row=1,column=1)

    def ing():
        u=usuario.get()
        c=contraseña.get()                          #iniciar sesión pt 1 y .get()
        i=iniciar_sesion(u,c)
        if i==False:
            messagebox.showwarning('ERROR','usuario o contraseña no validos')
        else:
            ventana21.destroy()
            ventana211(u)
        
    boton_i=Button(frame,text='ingresar', command=ing)
    boton_i.grid(row=2,column=0,columnspan=2,ipadx=80,pady=10)

    def vol():
        ventana21.destroy()
        ventana2()
        
    boton_r=Button(frame,text='volver',command=vol)
    boton_r.grid(row=3,column=0,columnspan=2,ipadx=85)
    
    mainloop()

#--------------------------------------ventana211------------------------------------------
def ventana211(n):
    def guardar():
        x=info.get('1.0',END)                   #guardar pt 3
        acum=''
        for i in x:
            y=ord(i)+1
            z=chr(y)
            acum=acum+z
            
        return acum
    nombre=n
    def añadir_info():
        añadirtex=open('cuenta '+nombre+'.txt','w')
        añadirtex.write(guardar())                  #guardar pt 2
        añadirtex.close()
    def leer_info():
        leertex=open('cuenta '+nombre+'.txt','r')
        info=leertex.readlines()                    #insertar texto guardado pt 2
        leertex.close()
        return info
    
    ventana211=tk.Tk()
    ventana211.title(f'{n}')
    ventana211.iconbitmap('tres-raya.ico')
    ventana211.config(bg='black')

    frame=Frame(ventana211)
    frame.config(bg='black')
    frame.pack()

    info=tk.Text(frame,width=50,height=10)              #texto largo

    info.config(bg='light goldenrod',font=('Tw Cen MT',20))

    for i in leer_info():
        for j in i:                                     #insertar texto guardado pt 1
            info.insert(tk.INSERT,chr(ord(j)-1))

    info.grid(row=1,column=0,ipady=5)
    deslizador=Scrollbar(frame,command=info.yview)      #deslizador
    deslizador.grid(row=1,column=1,sticky='nsew')
    info.config(yscrollcommand=deslizador.set)

    boton_g=Button(frame,text='guardar',command=añadir_info)    #guardar pt 1
    boton_g.grid(row=2,column=0,ipadx=350)

    def salir():
        ventana211.destroy()

    boton_s=Button(frame,text='salir',command=salir)
    boton_s.grid(row=2,column=1,ipadx=10)

    mainloop()

#--------------------------------------ventana22------------------------------------------
def ventana22():
    ventana22=tk.Tk()
    ventana22.title('Tic Tac Toe')
    ventana22.iconbitmap('tres-raya.ico')
    ventana22.config(bg='black')

    frame=Frame(ventana22)
    frame.config(bg='black')
    frame.pack(pady=30,padx=100)

    texto1=tk.Label(frame,text='Nuevo usuario')
    texto1.config(bg='black',fg='white')
    texto1.grid(row=0,column=0,pady=10)

    nusuario=tk.Entry(frame)
    nusuario.config(justify='center')
    nusuario.grid(row=0,column=1)

    texto2=tk.Label(frame,text='contraseña')
    texto2.config(bg='black',fg='white')
    texto2.grid(row=1,column=0,pady=10)

    ncontraseña=tk.Entry(frame)
    ncontraseña.config(justify='center')
    ncontraseña.grid(row=1,column=1)

    def reg():                                      #registrar pt 2
        u=nusuario.get()
        c=ncontraseña.get()
        r=registrar(u,c)
        if r==False:
            messagebox.showwarning('ERROR','usuario ya registrado') #registrar pt 4
        else:
            n_cuenta=open('cuenta '+u+'.txt','w')
            n_cuenta.close
            ventana22.destroy()
            ventana2()
        
    boton_r=Button(frame,text='registrar',command=reg)              #registrar pt 1
    boton_r.grid(row=2,column=0,columnspan=2,ipadx=80,pady=10)

    def vol():
        ventana22.destroy()
        ventana2()
        
    boton_r=Button(frame,text='volver',command=vol)
    boton_r.grid(row=3,column=0,columnspan=2,ipadx=85)

    mainloop()
#---------------------------------organizador cuentas----------------------------------------
def comprobar_archivo():
    if (os.path.isfile("cuentas.txt")):
        return True
    else:
        txt=open('cuentas.txt','w')
        txt.close()
        
def leer_cuentas():
    tex=open('cuentas.txt','r')
    infotex=tex.read()
    tex.close()
    list_us_co=infotex.split()

    for i in list_us_co:
        list_cada_us_co=i.split('-->')
        us=list_cada_us_co[0]
        co=list_cada_us_co[1]
        dicc_us_co[us]=co
        
##def inf_anterior(x,y):
##    for i in range(len(x)):
##        tex=open('cuentas.txt','a')
##        tex.write(x[i]+'-->'+y[i]+'\n')
##        tex.close()
        
def registrar(u,c):
    global dicc_us_co                       #registrar pt 3 y diccionario

    cont=0
    for i in dicc_us_co.keys():             #diccionario usuarios
        uc=''
        for j in u:
            x=chr(ord(j)+1)
            uc=uc+x
            
        if uc==i:
            no=True
        else:
            cont=cont+1
    if cont==len(dicc_us_co.keys()):

        uc=''
        for i in u:
            x=chr(ord(i)+1)
            uc=uc+x
            
        cc=''
        for i in c:
            y=chr(ord(i)+1)
            cc=cc+y
            
        dicc_us_co[uc]=cc           #agregar a diccionario
        añadir_cuenta(uc,cc)        #añadir cuenta pt 1
        return True
    if no==True:
        return False
    
def añadir_cuenta(u,c):
    escribirtex=open('cuentas.txt','a')     #añadir cuenta pt 2
    escribirtex.write(u+'-->'+c+'\n')
    escribirtex.close()

def iniciar_sesion(u,c):                    #iniciar sesión pt 2
    si=False
    cont=0
    for i in dicc_us_co.keys():
        ud=''
        for j in i:
            x=chr(ord(j)-1)                 #decodificación
            ud=ud+x
        if ud==u:
            si=True
        else:
            cont=cont+1
            
    if cont==len(dicc_us_co.keys()):
        cont=0
        a=False
    if si==True:
        a=True

    uc=''
    for j in ud:
        x=chr(ord(j)+1) 
        uc=uc+x                             #codificación
    cc=''
    for j in c:
        x=chr(ord(j)+1)
        cc=cc+x
        
    if dicc_us_co.get(uc,'Contraseña incorrecta')==cc:
        b=True
    if dicc_us_co.get(uc,'Contraseña incorrecta')!=cc:
        b=False
        
    if a==True and b==True:
        return True
    if a==False or b==False:
        return False
    

comprobar_archivo() #comp archivos
dicc_us_co={}       #creación diccionario
leer_cuentas()
##us_en_tex=list(dicc_us_co.keys())
##co_en_tex=list(dicc_us_co.values())
##inf_anterior(us_en_tex,co_en_tex)

##----------------------------inicio----------------------------------------------------
ventana0()
