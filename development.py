# Блок импорта нужных либ
import tkinter as tk
from random import randint


# Глобальные переменные
global wd_flag
wd_flag = False

# Блок функций
def cypher():

    pass


def uncypher():
    pass


def clicked():
    pass


# Блок взаимодействия с пользователем
def in_development():
    window1 = tk.Tk()
    greeting = tk.Label(text="Вас приветствует инструмент Цезаря для шифрования и дешифрования. "
                             "Пожалуйста, выберите функцию.",
                        font=("Times New Roman", 16),
                        fg="green4",
                        bg="gray5")
    greeting.grid(row=0, column=1)

    cypher_button = tk.Button(text="Зашифровать сообщение",
                              font=("Times New Roman", 12),
                              fg="green4",
                              bg="gray5",
                              command=clicked())
    cypher_button.grid(row=1, column=0)

    uncypher_button = tk.Button(text="Расшифровать сообщение",
                                font=("Times New Roman", 12),
                                fg="green4",
                                bg="gray5",
                                command=clicked())
    uncypher_button.grid(row=1, column=2)

    text_entry_label = tk.Label(text="Введите ваше сообщение",
                                fg="green4",
                                bg="gray5")
    window1.mainloop()
    # if wd_flag == True:
       # window1.destroy()
        # wd_flag = False
        # window2 = tk.Tk()
        # text_entry = tk.Text(fg="green4",
         #                     bg="gray6")
       #  text_entry.pack()
        # window2.mainloop()


