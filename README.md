# python_study_things

Учебный репозиторий: конспекты и практические задания по Python и backend-разработке.
Это не готовая библиотека, а рабочая тетрадь — код по темам, который я пишу в процессе обучения.

Python 3.12 · управление зависимостями через [uv](https://docs.astral.sh/uv/)

## Содержание

| Раздел | О чём |
| :-- | :-- |
| [`SOLID/`](SOLID) | Принципы SRP и OCP: разбиение «god-объекта» и замена `if/elif` на полиморфизм |
| [`patterns/`](patterns) | Паттерны и приёмы проектирования (см. ниже) |
| [`pytest/`](pytest) | Практика тестирования: базовые тесты, моки, фикстуры |
| [`SQL/`](SQL) | Конспект по основам SQL и скрипт демонстрационной базы |
| [`oop/`](oop) | ООП: классы с docstring-тестами, решение проблемы forward references |
| [`OOP_book/`](OOP_book) | Задания по книге: mixins и `Protocol` |
| [`decorators/`](decorators) | Наглядная демонстрация работы `hashlib` |
| [`multiprocessing/`](multiprocessing) | Сравнение последовательного и многопроцессного выполнения CPU-bound задач |

### patterns/

| Тема | Папка | Содержание |
| :-- | :-- | :-- |
| Dependency Injection | `Dependency Enjection/` | FastAPI `Depends`, зависимости с `yield` и управлением ресурсами |
| Service & Repository | `service_and_repository_patterns/` | Слои service и repository, абстрактный репозиторий, Pydantic-схемы |
| Декораторы | `decorator/` | `timeit`, `retry`, кэширование, async-декоратор, декоратор с аргументами |

### pytest/

| Тема | Папка | Содержание |
| :-- | :-- | :-- |
| Основы | `basic/` | `assert`, параметризация, тестирование функции с внешним вызовом |
| Mock | `Mock/` | Изоляция зависимостей через моки |
| Фикстуры | `fixtures/` | Фикстуры, in-memory БД на SQLAlchemy, собственные исключения |

## Запуск

Установить зависимости:

```bash
uv sync
```

Запустить тесты:

```bash
uv run pytest
```

Отдельные упражнения — самостоятельные скрипты, их можно запускать напрямую:

```bash
uv run python multiprocessing/main.py
```
