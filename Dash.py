import tkinter as tk
import random

#Finestra principale
window = tk.Tk()
window.title("Ferrari F1 DashBoard")
window.geometry("648x380")
window.config(bg='black')

#Aggiornare dinamicamente i valori della finestra
def aggiorna_label(label, minimo, massimo, intervallo):
    valore = random.randint(minimo, massimo)
    label.config(text=str(valore))
    # Richiama se stessa dopo 'intervallo' ms
    label.after(intervallo, aggiorna_label, label, minimo, massimo, intervallo)

#PRIMA RIGA

#Quadrante del lap time
frame1 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame1.place (x=0,y=0, width=240, height=75)

label1 = tk.Label(frame1, text="01:12:378", fg = "Green2", bg = "black", font=("Arial", 30,"bold"))
label1.place(relx=0.5,rely=0.5, anchor="center")


#Quadrante giri motore
frame2 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame2.place (x=216,y=0, width=240, height=75)

label_giriMotore = tk.Label(frame2, text="11500", fg = "red2", bg = "black", font=("Arial", 41))
label_giriMotore.place(relx=0.5,rely=0.5,anchor="center")


#Quadrante delta time
frame3 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame3.place (x=432,y=0, width=217, height=75)

label_deltaTime = tk.Label(frame3, text="+10.365", fg = "Green2", bg = "black", font=("Arial", 30, "bold"))
label_deltaTime.place(relx=0.5,rely=0.5, anchor="center")



#SECONDA RIGA

#SPEED
frame4 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame4.place (x=0,y=73, width=160, height=85)

label4 = tk.Label(frame4, text="SPEED", fg="white", bg="black", font=("Arial", 10, "bold"))
label4.pack(anchor="nw", padx=2, pady=1)


label_speedValue = tk.Label(frame4, text="230", fg="white", bg="black", font=("Arial", 45, "bold"))
label_speedValue.pack(anchor="ne")


#Temp gomme alto sx
frame8 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame8.place (x=159,y=73, width=75, height=85)


label8 = tk.Label(frame8, text="40", fg = "red2", bg = "black", font=("Arial", 20, "bold"))
label8.place(relx=0.5,rely=0.5, anchor="center")


#Temp gomme basso sx
frame12 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame12.place (x=420,y=73, width=75, height=85)


label12 = tk.Label(frame12, text="40", fg = "red2", bg = "black", font=("Arial", 20, "bold"))
label12.place(relx=0.5,rely=0.5, anchor="center")


#BBAL
frame14 = tk.Frame(window,bg="black", highlightbackground="white", highlightthickness=2)
frame14.place(x=494,y=73, width=155, height=85)

label14 = tk.Label(frame14, text="BBAL", fg="white", bg="black", font=("Arial", 10, "bold"))
label14.pack(anchor="ne", padx=2, pady=1)


label15 = tk.Label(frame14, text="55.5", fg="white", bg="black", font=("Arial", 45, "bold"))
label15.pack(anchor="ne")




#TERZA RIGA

#LAP
frame5 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame5.place (x=0,y=157, width=160, height=85)


label6 = tk.Label(frame5, text="LAP", fg="white", bg="black", font=("Arial", 10, "bold"))
label6.pack(anchor="nw", padx=2, pady=1)


label7 = tk.Label(frame5, text="14", fg="white", bg="black", font=("Arial", 45, "bold"))
label7.pack(anchor="ne")



#Temp gomme alto dx
frame9 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame9.place (x=159,y=157, width=75, height=85)


label9 = tk.Label(frame9, text="40", fg = "red2", bg = "black", font=("Arial", 20, "bold"))
label9.place(relx=0.5,rely=0.5, anchor="center")



#Temp gomme basso dx
frame13 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame13.place (x=420,y=157, width=75, height=85)


label14 = tk.Label(frame13, text="40", fg = "red2", bg = "black", font=("Arial", 20, "bold"))
label14.place(relx=0.5,rely=0.5, anchor="center")


#PIT LIMITER
frame15 = tk.Frame(window, bg="red", highlightbackground="white", highlightthickness=2)
frame15.place (x=494,y=157, width=155, height=85)

label7 = tk.Label(frame15, text="PIT LIMIT", fg="white", bg="red", font=("Arial", 24, "bold"))
label7.place(relx=0.5,rely=0.5,anchor="center")





#SECONDA E TERZA RIGA

#GEAR
frame10 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame10.place (x=232,y=73, width=190, height=169)


label10 = tk.Label(frame10, text="GEAR", fg="white", bg="black", font=("Arial", 10, "bold"))
label10.pack(anchor="nw", padx=2, pady=1)


label11 = tk.Label(frame10, text="5", fg="white", bg="black", font=("Arial", 100, "bold"))
label11.pack(anchor="center")




#QUARTA RIGA

frame6 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame6.place (x=0,y=240, width=160, height=85)

# Label "SOC"
label6 = tk.Label(frame6, text="SOC", fg="white", bg="black", font=("Arial", 10, "bold"))
label6.pack(anchor="nw", padx=2, pady=1)

# Label valore "100"
label7 = tk.Label(frame6, text="100", fg="green2", bg="black", font=("Arial", 45, "bold"))
label7.pack(anchor="ne")


#MIX
frame16 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame16.place (x=159,y=240, width=65, height=85)

# Label "SOC"
label16 = tk.Label(frame16, text="MIX", fg="white", bg="black", font=("Arial", 10, "bold"))
label16.pack(anchor="nw", padx=2, pady=1)


label17 = tk.Label(frame16, text="2", fg="white", bg="black", font=("Arial", 45, "bold"))
label17.pack(anchor="ne")


#CURRENT LAP TIME
frame17 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame17.place (x=222,y=240, width=210, height=85)


label17 = tk.Label(frame17, text="01:04:32", fg="yellow", bg="black", font=("Arial", 25, "bold"))
label17.pack(padx=0.5, pady=0.5, anchor="center")


#ERS
frame18 = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2)
frame18.place (x=430,y=240, width=65, height=85)


label18 = tk.Label(frame18, text="ERS", fg="white", bg="black", font=("Arial", 10, "bold"))
label18.pack(anchor="ne", padx=2, pady=1)

label19 = tk.Label(frame18, text="3", fg="white", bg="black", font=("Arial", 45, "bold"))
label19.pack(anchor="ne")



#VSC
frame20 = tk.Frame(window, bg="yellow", highlightbackground="yellow", highlightthickness=2)
frame20.place (x=495,y=240, width=155, height=85)

label7 = tk.Label(frame20, text="VSC", fg="black", bg="yellow", font=("Arial",45, "bold"))
label7.place(relx=0.5,rely=0.5,anchor="center")




#Quinta riga: generazione delle luci del cambio
for i in range(20):
    
    if i <= 3:
       frame= tk.Frame(window, bg="red", highlightbackground="white", highlightthickness=1)
    elif i>=5 and i<=15:
        frame= tk.Frame(window, bg="green", highlightbackground="white", highlightthickness=1)
    else:
        frame= tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=1)
    frame.place(x=0+i*32.5,y=325 ,width=32.4, height=50)
    
    
aggiorna_label(label_giriMotore,3000,12000,1000)
aggiorna_label(label_speedValue,65,365,1000)   


    
window.mainloop()