import requests

# city, time(data), temp, condition


def get_weather(city, api='f32db3de351b336b12c38ab899e31f98'):

    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api}&units=metric'

    search = requests.get(url)
    content = search.json()

    lista = content['list']

    for dictionary in lista:
        with open('data.txt', 'a') as file:
            file.write(f"{city}, {dictionary['main']['temp']}, {dictionary['dt_txt']}, "
                       f"{dictionary['weather'][0]['description']},\n")


in_city = input('Write the city: ')

get_weather(in_city)
