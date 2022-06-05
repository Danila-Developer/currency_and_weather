import requests
import sqlite3


def fetch_currency():
    """
    Делает запрос к БД и, если сегоднящняя дата существует, возвращает список курсов,
    иначе отправляет запрос на сервер и записывает данные в БД, возвращая тот же словарь
    """
    db_connection = sqlite3.connect('db.sqlite3')
    cursor = db_connection.cursor()

    cursor.execute("select * from Currency_currency where date_of = date('now');")
    result = cursor.fetchone()

    if result is None:
        try:
            response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
            USD_value = round(1/(float(response.json()['rates']['USD'])), 2)
            EUR_value = round(1/(float(response.json()['rates']['EUR'])), 2)
            CHF_value = round(1/(float(response.json()['rates']['CHF'])), 2)
            all_currencies = [
                ('USD', USD_value),
                ('EUR', EUR_value),
                ('CHF', CHF_value)
            ]
            cursor.executemany("insert into Currency_currency (currency_name, currency_value) values (?, ?);", all_currencies)
            db_connection.commit()
        except requests.exceptions.ConnectionError:
            return ['error', 'ConnectionError']
    else:
        cursor.execute("select * from Currency_currency where date_of = date('now');")
        result = cursor.fetchall()
        all_currencies = []
        for row in result:
            all_currencies.append((row[1], row[2]))
    return all_currencies


def get_currency(all_currencies, currency_name):
    """Возвращает значение выбранной валюты из списка всех валют"""

    for currency in all_currencies:
        if currency[0] == currency_name:
            return currency[1]








