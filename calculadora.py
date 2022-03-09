from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor, heading, width

#cores utilizadas 

cor1= "#0a0a0a" #preto
cor2= "#132b94" #azul
cor3= "#b5aeb2" #cinza
cor4= "#82a1f5" #azul claro
cor5= "#ffffff" #branco


janela =Tk()
janela.title("Calculadora")
janela.geometry("264x330")
janela.config(bg=cor1)

#frames

visor = Frame(janela, width=264, height=50, bg=cor2)
visor.grid(row=0, column=0,)

discador = Frame(janela, width=264, height=280)
discador.grid(row=1, column=0,)

#função

numeros_tela = ""

#numeros visor

valor = StringVar()

def selecao_numeros(event):

    global numeros_tela

    numeros_tela=numeros_tela + str(event)
    

    valor.set(numeros_tela)
    

#funcao de calculo

def calcular():
    global numeros_tela
    resultado= eval(numeros_tela)
    
    valor.set(str(resultado))

#funcao de limpar tela
    
def limpar_tela():
    global numeros_tela
    numeros_tela= ""
    valor.set("")
    



numeros = Label(visor, textvariable=valor, width=16, height=2, bg=cor2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), fg=cor5)
numeros.place(x=15,y=0)

#botões

botao0= Button(discador,command= lambda: selecao_numeros("%"), text="%", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao0.place(x=0, y=0)

botao1= Button(discador,command= limpar_tela,text="CE", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao1.place(x=66, y=0)

botao2= Button(discador, command= limpar_tela,text="C", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao2.place(x=132, y=0)

botao3= Button(discador, command= lambda: selecao_numeros("/"),text="/", width=8, height=3, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao3.place(x=198, y=0)

botao4= Button(discador, command= lambda: selecao_numeros("7"),text="7", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=0, y=56)

botao5= Button(discador, command= lambda: selecao_numeros("8"),text="8", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao5.place(x=66, y=56)

botao6= Button(discador, command= lambda: selecao_numeros("9"),text="9", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao6.place(x=132, y=56)

botao7= Button(discador, command= lambda: selecao_numeros("*"),text="x", width=8, height=3, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=198, y=56)

botao8= Button(discador, command= lambda: selecao_numeros("4"),text="4", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=0, y=112)

botao9= Button(discador, command= lambda: selecao_numeros("5"),text="5", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=66, y=112)

botao10= Button(discador, command= lambda: selecao_numeros("6"),text="6", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=132, y=112)

botao11= Button(discador, command= lambda: selecao_numeros("-"),text="-", width=8, height=3, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=198, y=112)

botao8= Button(discador, command= lambda: selecao_numeros("1"),text="1", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=0, y=168)

botao9= Button(discador, command= lambda: selecao_numeros("2"),text="2", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=66, y=168)

botao10= Button(discador, command= lambda: selecao_numeros("3"),text="3", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=132, y=168)

botao11= Button(discador, command= lambda: selecao_numeros("+"),text="+", width=8, height=3, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=198, y=168)

botao8= Button(discador, command= lambda: selecao_numeros("0"),text="0", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=0, y=224)

botao9= Button(discador, command= lambda: selecao_numeros("."),text=".", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=66, y=224)

botao10= Button(discador, command= lambda: selecao_numeros(","),text=",", width=8, height=3, bg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=132, y=224)

botao11= Button(discador, command= calcular,text="=", width=8, height=3, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=198, y=224)





janela.mainloop()