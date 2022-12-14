import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# cors --------------------------------
co0 = "#FFFFFF"  # white
co1 = "#333333"  # black
co2 = "#fcc058"  # orange
co3 = "#fff873"  # yellow
co4 = "#34eb3d"   # green
co5 = "#e85151"   # red


fundo = "#3b3b3b"


janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=200, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)


app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)


app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_pc = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pc.place(x=190, y=10)

global voce
global pc 
global rounds
global pt_voce
global pt_pc

pt_voce = 0
pt_pc = 0
rounds = 5
#-----------LÓGICA-----------#
def jogar(i):
  global rounds
  global pt_voce
  global pt_pc


  if rounds > 0:
    print(rounds)
    option = ['Pedra', 'Papel', 'Tesoura']
    pc = random.choice(option)
    voce = i

    app_pc['text'] = pc
    app_pc['fg'] = co1


    if voce == 'Pedra' and pc == 'Pedra':
      print('empate')
      app_linha['bg'] = co3
      app_1_linha['bg'] = co0
      app_2_linha['bg'] = co0
    elif voce == 'Papel' and pc == 'Papel':
      print('empate')
      app_linha['bg'] = co3
      app_1_linha['bg'] = co0
      app_2_linha['bg'] = co0
    elif voce == 'Tesoura' and pc == 'Tesoura':
      print('empate')
      app_linha['bg'] = co3
      app_1_linha['bg'] = co0
      app_2_linha['bg'] = co0
    


    elif voce == 'Pedra' and pc == 'Tesoura' or voce == 'Papel' and pc == 'Pedra' or voce == 'Tesoura' and pc == 'Papel':
      print('Você ganhou')
      app_linha['bg'] = co0
      app_1_linha['bg'] = co4
      app_2_linha['bg'] = co5
      pt_voce += 10
      rounds -=1

    elif voce == 'Pedra' and pc == 'Papel' or voce == 'Papel' and pc == 'Tesoura' or voce == 'Tesoura' and pc == 'Pedra':
      print('Computador ganhou')
      app_linha['bg'] = co0
      app_1_linha['bg'] = co5
      app_2_linha['bg'] = co4
      pt_pc += 10
      rounds -=1

    app_1_pontos['text'] = pt_voce
    app_2_pontos['text'] = pt_pc
    
  
  
  else:
    app_1_pontos['text'] = pt_voce
    app_2_pontos['text'] = pt_pc


    game_over()


#--------INICIAR-JOGO---------#
def iniciar_jogo():
  global icon_1
  global icon_2
  global icon_3
  global b_icon_1
  global b_icon_2
  global b_icon_3

  b_jogar.destroy()

  icon_1 = Image.open('img/pedra.png')
  icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
  icon_1 = ImageTk.PhotoImage(icon_1)
  b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
  b_icon_1.place(x=15, y=60)

  icon_2 = Image.open('img/papel.png')
  icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
  icon_2 = ImageTk.PhotoImage(icon_2)
  b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
  b_icon_2.place(x=90, y=60)

  icon_3 = Image.open('img/tesoura.png')
  icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
  icon_3 = ImageTk.PhotoImage(icon_3)
  b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
  b_icon_3.place(x=170, y=60)




#-----------FIM-------------#
def game_over():
  global rounds
  global pt_voce
  global pt_pc

  pt_voce = 0 
  pt_pc = 0 
  rounds = 5

  b_icon_1.destroy()
  b_icon_2.destroy()
  b_icon_3.destroy()

  jogador_voce = int(app_1_pontos['text'])
  jogador_pc = int(app_2_pontos['text'])

  if jogador_voce > jogador_pc:
    app_vencedor = Label(frame_baixo, text="Parábens, você venceu!", height=2, anchor='center', font=('Ivy 12 bold'), bg=co0, fg=co4)
    app_vencedor.place(x=40, y=60)

  elif jogador_voce < jogador_pc:
      app_vencedor = Label(frame_baixo, text="Infelizmente, você perdeu!", height=2, anchor='center', font=('Ivy 12 bold'), bg=co0, fg=co5)
      app_vencedor.place(x=30, y=60) 


  def jogar_novamente():
    app_1_pontos['text'] = '0'
    app_2_pontos['text'] = '0'
    app_vencedor.destroy()
    b_jogar_novamente.destroy()

    iniciar_jogo()


  b_jogar_novamente = Button(frame_baixo, command=jogar_novamente, width=30, text='JOGAR NOVAMENTE!',  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
  b_jogar_novamente.place(x=5, y=140)



#----------ESCOLHAS-----------#


b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='JOGAR',  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=140)

janela.mainloop()