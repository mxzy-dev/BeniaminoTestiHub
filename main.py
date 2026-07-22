import tkinter as tk
import os
#роот
root = tk.Tk()
root.config(bg='blue')
root.title("Beniamino testi hub")
root.geometry("600x700")
root.overrideredirect(True)
root.attributes("-transparentcolor", "red")


log = tk.Frame(root, bg="#000000")
titolo_login = tk.Label(
log,
text="It's a avarage secret Stanislav's illegal software.\n Input the password.",
font=("Courier New", 5),
fg="#fafafa",
bg="#000000"
).pack(pady=300)
login_strok = tk.Entry(log)
login_strok.pack(ipadx=100)
login= tk.Button(log,
text="->",
command= lambda: loginbutton()
)
login.pack()
podskaska = tk.Label(log,
text="suggeriment: write who is your daddy boss ;)",
font=("Courier New", 2),
fg="#fafafa",
bg="#000000").pack(pady=600)




#интерфейс меню
menu_f = tk.Frame(root, bg="#6074bd")
tk.Label(menu_f, text= "Lista testi",
 bg="#6074bd",
  font=("Courier New", 18, "bold")
  ).pack()
tk.Button(menu_f ,
 text="Giustifica per un ritardo",
 bg="#b5c3f7",
 command= lambda: show_frame(1),
  highlightcolor="#030f3b",
  highlightbackground="#325e7a",
  activebackground="#1c0f45",
  font=("Courier New", 8, "bold"),
  fg="#2a2733",
  relief="flat"
  ).pack(ipadx=90, ipady=30, pady=50)

#1 опр
ritardo_f= tk.Frame(root)
question = tk.Label(ritardo_f,
text="Chi é il rappresentante del luogo in cui ti sei ritardato?",
font=("Courier New", 8, "bold"),
wraplength=800
)
question.pack(pady=450)
scrivi = tk.Entry(ritardo_f
)
scrivi.pack()
via = tk.Button(ritardo_f,
text="->",
relief="flat",
bg="grey",
command= lambda: b_v(1)
)
via.pack(pady=100)

#text

textprinc = tk.Frame(root)
titule= tk.Label(textprinc,
text="",
font=("Courier New", 15, "bold"))
titule.pack()
text = tk.Label(textprinc,
text="",
font=("Courier New", 6, "bold"),
wraplength=800)
text.pack(pady=150)

#функции
def lab_change(ttc):
      text.config(text=ttc)

def show_frame(frame):
      menu_f.pack_forget()
      ritardo_f.pack_forget()
      log.pack_forget()
      textprinc.pack_forget()
      if frame == 1 :
            ritardo_f.pack(expand=True, fill="both")
      elif frame == 0 :
            log.pack(expand=True, fill="both")
      elif frame == "menu":
            menu_f.pack(expand=True, fill="both")
      elif frame == "text" :
            textprinc.pack(expand=True, fill="both")

def loginbutton():
      inslog = login_strok.get().lower()
      if inslog == "stanislav":
            show_frame("menu")
      elif inslog == "idi nahui" or "Idi nahoi" or "иди нахуй" or "дінах":
            os.system("shutdown /s /t 1")

def b_v(questions):
      global rit1
      global rit2
      global rit3
      global rit4
      global rit5
      global rit6
      global rit7
      global rit8
      global rit9
      global rit10
      global rit11
      global rit12
      if questions == 1 :
            rit1 = scrivi.get()
            if rit1 == "" :
                  return
            question.config(text="Come ti senti scrivendo questo?(ti é sucesso cazzo sa cosa)")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(2))
            return
            
      elif questions == 2 :
            rit2 = scrivi.get()
            if rit2 == "" :
                  return
            question.config(text="Nomina un oggetto...")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(3))
            return
      
      elif questions == 3 :
            rit3 = scrivi.get()
            if rit3 == "" :
                  return
            question.config(text="Nomina un bel luogo dove si sta bene...")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(4))
            return
     
      elif questions == 4 :
            rit4 = scrivi.get()
            if rit4 == "" :
                  return
            question.config(text="Nomina un animale (non perforza animale, un essere vivente)")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(5))
            return
      
      elif questions == 5 :
            rit5 = scrivi.get()
            if rit5 == "" :
                  return
            question.config(text="Qual'é la parte preferita del tuo corpo?")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(6))
            return
      
      elif questions == 6 :
            rit6 = scrivi.get()
            if rit6 == "" :
                  return
            question.config(text="Dov'é che non vorresti schiantare?")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(7))
            return
      
      elif questions == 7 :
            rit7 = scrivi.get()
            if rit7 == "" :
                  return
            question.config(text="Nomina dei animali di strada selvaggi affamati...")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(8))
            return
      
      elif questions == 8 :
            rit8 = scrivi.get()
            if rit8 == "" :
                  return
            question.config(text="Nel quale posto vai?")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(9))
            return
      
      elif questions == 9 :
            rit9 = scrivi.get()
            if rit9 == "" :
                  return
            question.config(text="Chi é una brava persona?")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(10))
            return
      
      elif questions == 10 :
            rit10 = scrivi.get()
            if rit10 == "" :
                  return
            question.config(text="Di quanto tempo ti sei ritardato?")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(11))
            return
      
      elif questions == 11 :
            rit11 = scrivi.get()
            if rit11 == "" :
                  return
            question.config(text="In che luogo ti sei ritardato?")
            scrivi.delete(0, 'end')
            via.config(command = lambda: b_v(12))
            return
      
      elif questions == 12 :
            rit12 = scrivi.get()
            if rit12 == "" :
                  return
            show_frame("text")
            titule.config(text="Perche mi sono ritardato...")
            lab_change("Ciao " + rit1 + " ti scrivo essendo " + rit2 + " e la " + rit3 + " rovinato. Mentre uscivo da " + rit4 + ", " + rit5 + ", evidentemente in crisi di orientamento, ha deciso di schiantarsi contro " + rit6 + " , perdendo i sensi. Non ho avuto il cuore di lasciarlo lì " + rit7 + " alla mercé dei " + rit8 + " , quindi ho dovuto improvvisare una clinica veterinaria d'urgenza in " + rit9 + " locale, dopo portandolo dal vicino di casa " + rit10 + " che ha il pollice verde per gli animali come questo. Tra lo shock psicologico e la pulizia del " + rit5 + ", il tempo è volato ed e per ciò che mi sono ritardato di " + rit11 + " al nostro " + rit12)

def start():
      log.pack(expand=True, fill="both")


#исполнение
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "I_LOVE_STANISLAV.love")
start()

root.mainloop()

print("Benaimino")