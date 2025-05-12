import tkinter as tk
import random

def aggiorna_label(label, minimo, massimo, intervallo):
    valore = random.randint(minimo, massimo)
    label.config(text=str(valore))
    # Richiama se stessa dopo 'intervallo' ms
    label.after(intervallo, aggiorna_label, label, minimo, massimo, intervallo)

# Finestra
window = tk.Tk()
window.configure(bg="black")

# Frame SPEED
frame_speed = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2, width=120, height=80)
frame_speed.pack(padx=10, pady=10)
frame_speed.pack_propagate(False)

tk.Label(frame_speed, text="SPEED", fg="white", bg="black", font=("Arial", 10, "bold")).pack(anchor="nw", padx=2, pady=1)
label_speed = tk.Label(frame_speed, text="0", fg="white", bg="black", font=("Arial", 32, "bold"))
label_speed.pack(expand=True)

# Frame RPM
frame_rpm = tk.Frame(window, bg="black", highlightbackground="white", highlightthickness=2, width=120, height=80)
frame_rpm.pack(padx=10, pady=10)
frame_rpm.pack_propagate(False)

tk.Label(frame_rpm, text="RPM", fg="white", bg="black", font=("Arial", 10, "bold")).pack(anchor="nw", padx=2, pady=1)
label_rpm = tk.Label(frame_rpm, text="0", fg="white", bg="black", font=("Arial", 32, "bold"))
label_rpm.pack(expand=True)

# Avvia aggiornamenti
aggiorna_label(label_speed, 100, 350, 5000)   # Simula velocità
aggiorna_label(label_rpm, 3000, 12000, 5000)  # Simula RPM

window.mainloop()
