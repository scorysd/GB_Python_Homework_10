import yahoo_fin.stock_info as si
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

def convert_currency_yahoofin(src, dst, amount):
    symbol = f"{src}{dst}=X"
    latest_data = si.get_data(symbol, interval="1m", start_date=datetime.now() - timedelta(days=2))
    last_updated_datetime = latest_data.index[-1].to_pydatetime()
    latest_price = latest_data.iloc[-1].close
    return last_updated_datetime, latest_price * amount

def callbackFunc1(event):
    global source_currency
    a = combo_box_1.get()
    source_currency = ""
    for i in range(3):
        source_currency += a[i]

def callbackFunc2(event):
    global destination_currency
    b = combo_box_2.get()
    destination_currency = ""
    for i in range(3):
        destination_currency += b[i]

def push():
    amount = float(amount_1.get())
    last_updated_datetime, exchange_rate = convert_currency_yahoofin(source_currency, destination_currency, amount)
    outpt['text'] = 'По состоянию на:', last_updated_datetime, amount, source_currency, '=', round(exchange_rate, 3), destination_currency

window = tk.Tk()
window.title('Конвертер валют')
window.geometry('380x375')
window['bg']='black'
window.resizable(width=False, height=False)
amount_1 = StringVar()

lbl = tk.Label(window, text="Введите сумму:", background="black")
lbl.grid(row=0, column=0)
lbl = tk.Label(window, text="Выберите исходную валюту:", background="black")
lbl.grid(row=1, column=0)
lbl = tk.Label(window, text="Выберите конечную валюту:", background="black")
lbl.grid(row=2, column=0)
inpt = tk.Entry(window, textvariable=amount_1, background="black", bd=False)
inpt.grid(row=0, column=1)
lst = [
    'RUB - рубль', 'USD - доллар', 'EUR - евро',
    'THB - тайский бат', 'AZN - азербайджанский манат',
    'AED - дирхам ОАЭ', 'CNY - китайский юань', 'ILS - израильский шекель'
]
combo_box_1 = ttk.Combobox(window, width=19, values=lst, state='readonly', background="black")
combo_box_1.grid(row=1, column=1, columnspan=2)
combo_box_1.bind("<<ComboboxSelected>>", callbackFunc1)
combo_box_2 = ttk.Combobox(window, width=19, values=lst, state='readonly', background="black")
combo_box_2.grid(row=2, column=1, columnspan=2)
combo_box_2.bind("<<ComboboxSelected>>", callbackFunc2)
outpt = tk.Label(window, wraplength=275, background="black")
outpt.grid(row=9, column=0, columnspan=2)
btn = tk.Button(window, text='Конвертировать', command= push, background="black", bd=0)
btn.grid(row=5, column=0, columnspan=2)
img = PhotoImage(file="1.png")
label = Label(window, image=img, background="black")
label.image_ref = img
label.grid(row=6, column=0, columnspan=2)
window.mainloop()