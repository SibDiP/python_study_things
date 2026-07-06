"""
Задача 4: Внедрение сервиса с параметрами (Depends)
Представь, что ты пишешь сервис для расчета стоимости доставки.

1. Создай класс PriceCalculator, который в конструкторе (__init__) принимает 
tax_rate: float. У класса должен быть метод calculate(amount: float), который 
возвращает amount * (1 + tax_rate).

2. Создай функцию-зависимость get_calculator(), которая возвращает 
экземпляр PriceCalculator с фиксированным налогом (например, 0.2).

3. Создай эндпоинт GET /calculate, который принимает amount как query-параметр, 
использует get_calculator через Depends и возвращает итоговую стоимость.

Зачем это нужно: Это учит тебя внедрять не просто функции, а целые 
объекты-сервисы, которые могут иметь свои настройки.
"""
from fastapi import FastAPI, Depends


app = FastAPI()

class PriceCalculator():
    def __init__(self, tax_rate: float) -> None:
        self.tax_rate = tax_rate
    
    def calculate(self, amount: float) -> float:
        return amount * (1 + self.tax_rate)

def get_calculator() -> PriceCalculator:
    tax_rate: float = 0.2
    return PriceCalculator(tax_rate)

@app.get('/calculate')
def calculate(
    amount: float, 
    calculator: PriceCalculator = Depends(get_calculator)
    ):
    final_price = calculator.calculate(amount)
    return final_price


"""
Задача 2: Управление временем жизни внешнего API клиента (yield)

Представь, что твое приложение должно общаться с внешним API (например, сервисом погоды).

1. Создай класс WeatherClient.
    •В методе __init__ он должен выводить: "WeatherClient: Установка соединения 
    с метеостанцией..."
    •У него должен быть метод get_weather(city: str), который возвращает 
    случайную температуру.
    •Добавь метод close(), который выводит: "WeatherClient: Соединение разорвано."

2. Создай зависимость get_weather_client() с использованием yield. Она должна 
создавать клиент, отдавать его в эндпоинт и гарантированно закрывать соединение 
в блоке finally.

3. Создай эндпоинт GET /weather/{city}, который использует этот клиент для 
получения погоды.

Зачем это нужно: Это классический сценарий использования yield для HTTP-клиентов
(например, httpx.AsyncClient ), где важно не плодить лишние соединения и вовремя 
их закрывать.

"""
from pydantic import BaseModel
import random
from fastapi import FastAPI, Depends


class WeatherClient:
    def __init__(self) -> None:
        print("WeatherClient: Установка соединения c метеостанцией...")
    
    def get_weather(self, city: str):
        return random.randrange(-50, 50)
    
    def close(self) -> None:
        print("WeatherClient: Соединение разорвано.")


def get_weather_client():
    weather_client_object = WeatherClient()
    try:
        yield weather_client_object
    finally:
        weather_client_object.close()

app = FastAPI()

@app.get('/weather/city/{city}')
def get_weather_in_a_city(
    city: str,
    weather_client: WeatherClient = Depends(get_weather_client)
):
    return weather_client.get_weather(city)