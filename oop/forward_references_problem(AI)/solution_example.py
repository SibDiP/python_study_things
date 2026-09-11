from __future__ import annotations

class Employee:
    # Теперь Python видит Boss, но не паникует. 
    # Он говорит: "Окей, это какая-то ссылка, разберусь позже".
    def __init__(self, name: str, boss: Boss):
        self.name = name
        self.boss = boss

class Boss:
    def __init__(self, name: str):
        self.name = name

# Создаем объекты
big_boss = Boss("Иван Иванович")
worker = Employee("Алексей", big_boss)

print(f"Работник: {worker.name}, Шеф: {worker.boss.name}")
# Результат: Работник: Алексей, Шеф: Иван Иванович
