"""
Задание 1: Базовое DI в FastAPI

Создай небольшое FastAPI приложение с двумя эндпоинтами:

1.
GET /health: Возвращает {"status": "ok"}.

2.
GET /greet/{name}: Принимает name как параметр пути. Используй 
функцию-зависимость get_greeting_message(), которая возвращает строку "Привет, "
. Эндпоинт должен возвращать полное приветствие (например, "Привет, Alice!").


"""

from fastapi import FastAPI, Depends


app = FastAPI()

@app.get('/health')
def health_check():
    return {'status': 'ok'}

def get_greeting_message() -> str:
    return "Привет, "

@app.get('/greet/{name}')
def greet_user(name: str, greeting: str = Depends(get_greeting_message)) -> str:
    return f"{greeting}{name}"
    
"""
Задание 2: DI с yield для управления ресурсом

Модифицируй приложение из Задания 1. Добавь новую зависимость get_file_logger(), 
которая имитирует открытие и закрытие файла для логирования. Эта зависимость 
должна использовать yield.

•Функция get_file_logger() должна:
    •Выводить в консоль "Открытие файла лога..." перед yield.
    •Возвращать объект, у которого есть метод log(message) (просто выводит сообщение в консоль).
    •Выводить в консоль "Закрытие файла лога." после yield.
•Создай новый эндпоинт POST /log_message, который принимает JSON с полем message 
и использует get_file_logger() для записи этого сообщения.
"""
from pydantic import BaseModel

class LogMessageSchema(BaseModel):
    message: str

class LogMessage:
    def log(self, message: str):
        print(f"Запись в лог: {message}")

def get_file_logger():
    print('Открытие файла лога...')
    log_object = LogMessage()
    try:
        yield log_object
    finally:
        print('Закрытие лога.')

@app.post('/log_message')
def log_message_endpoint(
    payload: LogMessageSchema, 
    my_logger = Depends(get_file_logger)
    ):
    my_logger.log(payload.message) 
    return {"status": "logged"}

"""
Задание 3: Переопределение зависимостей для тестирования

Напиши юнит-тест для эндпоинта POST /log_message из Задания 2. В тесте 
переопредели зависимость get_file_logger() на "заглушку" (MockFileLogger), 
которая просто выводит сообщение о том, что лог был записан в mock-объект, без 
реального открытия/закрытия файла.

•Убедись, что твой тест проверяет:
•Статус-код ответа (должен быть 200).
•Содержимое ответа (например, {"status": "logged"}).
"""

