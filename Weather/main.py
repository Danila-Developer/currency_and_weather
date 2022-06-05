from tkinter import Tk, Frame, Label, StringVar, Entry, Button, Text
from tkinter import messagebox as mb
import datetime
from Weather.model import get_weather_by_city

def set_weather_description(*args):
    """Устанавливает температуру и описание
    (также обрабатывает исключения "Нет сети" и "Город не идентифицировн")"""

    weather_info = get_weather_by_city(city_input_text.get())
    if weather_info[0] == 'error':
        if weather_info[1] == 'AttributeError':
            mb.showerror('Ошибка', 'Город однозначно не идентифицирован')
        else:
            mb.showerror('Ошибка', 'Проблемы с подключением')
    else:
        description_input.delete(1.0, 100.100)
        description_input.insert(1.0, weather_info[1])
        temperature_input_text.set(weather_info[0])

if __name__ == '__main__':
    root = Tk()
    root.title('Погода')

    input_frame = Frame(root)
    output_frame = Frame(root)

    city_label = Label(input_frame, text='Город')
    city_input_text = StringVar()
    city_input = Entry(input_frame, textvariable=city_input_text, width=40)

    date_label = Label(input_frame, text='Дата')
    date_input_text = StringVar()
    date_input = Entry(input_frame, textvariable=date_input_text, state='disabled', width=20)

    load_button = Button(text='Загрузить', command=set_weather_description)

    description_input_text = StringVar()
    description_input = Text(output_frame, height=10, width=40)
    temperature_label = Label(output_frame, text='Температура', width=10)
    temperature_input_text = StringVar()
    temperature_input = Entry(output_frame, textvariable=temperature_input_text, width=30)

    input_frame.grid(column=0, row=0, ipady=20)
    output_frame.grid(column=0, row=1)

    description_input.grid(column=0, row=2, columnspan=4)
    temperature_label.grid(column=0, row=0, columnspan=1)
    temperature_input.grid(column=1, row=0, columnspan=3)
    load_button.grid(row=3)
    city_label.grid(column=0, row=0)
    city_input.grid(column=1, row=0, columnspan=4)
    date_label.grid(column=0, row=1)
    date_input.grid(column=1, row=1, columnspan=2)

    now_date = datetime.datetime.today().strftime('%Y-%m-%d')
    date_input_text.set(now_date)

    root.mainloop()
