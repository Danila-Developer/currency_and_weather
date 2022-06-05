import tkinter as tk
from tkinter import ttk
from Currency.model import fetch_currency, get_currency
from tkinter import messagebox as mb

def change_currency(*args):
    """Изменяет значение курса валюты в зависимости от выбора в ComboBox"""
    if all_currencies[0] == 'error':
        mb.showerror('Ошибка', 'Нет подключения к сети')
    else:
        entryText.set(get_currency(all_currencies, currency_box.get()))

if __name__ == '__main__':
    all_currencies = fetch_currency()

    root = tk.Tk()
    root.title('Валюты')
    currency_name = tk.Label(root, text='Валюта')
    currency_box = ttk.Combobox(root, values=['USD', 'EUR', 'CHF'])
    course_name = tk.Label(root, text='Курс')
    entryText = tk.StringVar()
    course_value = tk.Entry(root, textvariable=entryText)

    currency_box.grid(column=1, row=0)
    currency_name.grid(column=0, row=0)
    course_name.grid(column=0, row=1)
    course_value.grid(column=1, row=1)

    currency_box.bind('<<ComboboxSelected>>', change_currency)

    root.mainloop()
