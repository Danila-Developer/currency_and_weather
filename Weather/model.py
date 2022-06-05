import requests
from bs4 import BeautifulSoup


def get_weather_by_city(city):
    """Возвращает информацию о погоде в выбранном городе"""
    try:
        html_response = requests.get('https://pogoda.mail.ru/search/?name=' + city).text
        soup = BeautifulSoup(html_response, 'lxml')
        temperature = soup.find('div', attrs={'class': 'information__content__temperature'}).contents[-1]
        temperature = str(temperature).split('\t')[0]
        about_weather_list = soup.findAll('div', attrs={'class': 'information__content__additional__item'})
        weather_description = (str(about_weather_list[1].contents[0]).split('\t')[8])
        about_weather = []
        for element in about_weather_list:
            for el in element.findAll('span'):
                about_weather.append(el.get('title'))
        for element in about_weather:
            if element is not None:
                weather_description = weather_description + element + '\n'
        return [temperature, weather_description]
    except AttributeError:
        return ['error', 'AttributeError']
    except requests.exceptions.ConnectionError:
        return ['error', 'ConnectionError']



