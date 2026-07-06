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

import pytest
from fastapi.testclient import TestClient
from base_di import app, get_file_logger


class MockLogMessage:
    def log(self, message):
        print(f"[MOCK] Лог записан: {message}")

@pytest.fixture
def client():
    # Создаем мок-зависимость
    def override_get_file_logger():
        try:
            yield MockLogMessage()
        finally:
            pass

    # Переопределяем зависимость перед запуском теста
    app.dependency_overrides[get_file_logger] = override_get_file_logger
    
    # Создаем и лениво отдаем клиент в тест
    with TestClient(app) as test_client:
        yield test_client
    
    # Этот код выполнится автоматически ПОСЛЕ завершения теста
    app.dependency_overrides.clear()

# 3. Сам тест. Мы просто передаем имя фикстуры 'client' в аргументы функции!
def test_log_message(client):
    payload = {"message": "Это успешный тест через pytest фикстуру"}
    
    response = client.post('/log_message', json=payload)
    
    assert response.status_code == 200
    assert response.json() == {"status": "logged"}