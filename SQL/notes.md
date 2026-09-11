Сcылка на курс 
https://www.youtube.com/watch?v=uGKIXTUjZbc&list=PLtPJ9lKvJ4oh5SdmGVusIVDPcELrJ2bsT

# 1

Типы Баз данных:
1) Сетевые и иерархические / LDAP, Microsoft Active Directory (AD)
2) Реляционные (отношение) - связанные таблицы / sql
3) Big Data, NoSQL - данные хранятся в неструктурированном виде на распределенном кластере серверов

Таблица включает столбцы (атрибуты)
- в строках содержатся отдельные сущности
- в ячейках только отдельные значения. Массивы и списки не приветствуются
- значения могут быть Null


SEQL -> SQL - Structured Query Language (язык структурированных запросов)
Плюсы:
- строгая математическая модель (реляционная модель данных, реляционная алгебра, реляционное исчисление)
- стандарты
- большая распространенность

Таблицы в SQL представляют из себя неупорядоченное множество значений.

# 2 Оператор SELECT
Ключевые слова блока:
SELECT - извлечение
FROM - источник
DISTINCT - выбор уникальных значений в столбцах
LIMIT - ограничение количества извлекаемых строк
AS - созданиме псевдонима для столбца


SELECT * FROM superheroes; 

SELECT name, appearances FROM superheroes


!tip - выход из результатов выборки в терминале на q

- Псевдонимы

1 Вариант - явный
SELECT name AS hero_name, appearances FROM superheroes  // столбец name -> hero_name

2 Вариант - не явный
SELECT name hero_name, appearances FROM superheroes

- Выбор уникальных значений столбцов

SELECT DISTICT(align) FROM superheroes 

- Ограничение количества извлекаемых строк

SELECT DISTINCT(HAIR)
FROM superheroes
LIMIT 10


info! - SQL - Декларативный язык. Говорим что хотим получить, а не как. Как - выбирает сервер в зависимости от того, что за сервер и какую технологию хранения мы используем.

# 3 Фильтрация с помощью WHERE

SELECT *
FROM superheroes
WHERE align = 'Reformed Criminals'

## Операторы:
= - равно
<>,!= неравно
> - больше
>= - больше или равно
< - меньше
<= - меньше или равно
between - значение в указанном диапазоне
in - значение входит в список
like - Проверка строки на соответсвие шаблону. Спец символы:
    % - любое количество символов
    _ - ровно один символ


- BETWEEN

SELECT *
FROM superheroes
WHERE year BETWEEN 2000 AND 2005

- IN
SELECT *
FROM superheroes
WHERE hair IN ('Red Hair', 'Blond Hair')

- LIKE
SELECT *
FROM superheroes
WHERE hair LIKE '%Blond%'


## Логические операции
AND
OR
NOT

- AND
SELECT *
FROM superheroes
WHERE gender = 'Female Characters'
    AND
    align = 'Bad Characters'

- OR
SELECT *
FROM superheroes
WHERE hair = 'Red Hair'
    OR hair = 'Strawberry Blond Hair'
    OR hair = 'Auburn Hair'


- NOT - можно использовать в комбинации
SELECT *
FROM superheroes
WHERE hair NOT IN ('Blond Hair', 'Black Hair', 'Brown Hair') OR hair IS NULL;


# 4 Сортировка в SQL: ORDER BY
!info - SELECT - извлекает данные, но не гарантирует упорядоченность

SELECT *
FROM superheroes
ORDER BY year

- Порядок сортировки:
    - ASC (ascending) - сортировка по возрастанию
    - DESC (descending) - сортировка по убыванию

...
ORDER BY appearances DESC


- СОРТИРОВКА И ФИЛЬТРЫ В SELECT
...
WHERE align = 'Bad Characters'
ORDER BY appearances DESC
LIMIT 5

- можно сортировать по нескольким критериям. 

...
ORDER BY year, appearances


- SQL похож на Аншийский. 
Не зря назывался SEQUEL (Structured English Query Language) 


# 5 Создание таблиц в SQL
## Кратко
    - Работа с таблицами
    CREATE TABLE
    DROP TABLE
    ALTER TABLE - изменить

    - Языки в SQL
    Data Definition Language (DDL) - CREATE/DROP/ALTER
    Data Manipulation language (DML) - SELECT/INSERT/DELETE
    Data Control Language (DCL) - Управление доступом к данным

    - Работа с таблицами отличается в разных реализациях

## Типы данных в SQL

CREATE TABLE superheroes(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    allign VARCHAR(30),

)

CHARACTER(n) (CHAR(n)) - Строка фиксированной длинны n
CHARACTER VARYING(n) (VARCHAR(n)) - Строка переменной длинны
BOOLEAN - Логический тип данных
INTEGER (INT) - Целое число
NUMERIC(p,s) - Действительное число 
    (p - количество значащих цифр, 
    s - количество цифр после запятой). Зранится точно.
REAL - действительное число одинарной точности (6 знаков после запятой), формат IEEE 754
DOUBLE PRECISION - действительное число двойной точности (15 знаков после запятой), формат IEEE 754
DATE - дата (год, месяц, число) 
    - '2026-08-13' 
TIMESTAMP - Дата и время
    - '2026-08-13 19:45:00' 
    - 'NOW'                    (специальное слово в Postgres для текущего времени)
...


## Первичный ключ в таблице
- уникальный идентификатор
CREATE TABLE superheroes(
    id INT PRIMARY KEY,
    ...
)

- SERIAL - СТАРЫЙ!!! тип данных обозначающий int который для каждой новой записи будет со значением +1. Верно только для Postgre - в других иначе слово.

CREATE TABLE superheroes(
    id SERIAL PRIMARY KEY,
    ...
)

- IDENTITY - новый стандарт.
    - GENERATED BY DEFAULT AS IDENTITY — позволяет вставить свое ID вручную, только если вы явно этого хотите (как и SERIAL, но более явно).
    - GENERATED ALWAYS AS IDENTITY — жесткий режим. Если вы попытаетесь вручную передать ID в запросе INSERT, база данных выдаст ошибку и запретит запись. Заставить ее принять ваше число можно будет только со специальным флагом OVERRIDING SYSTEM VALUE.

CREATE TABLE superheroes (
    id INT GENERATED BY DEFAULT AS IDENTITY
);


## Просмотр сведений о таблице

\d  - Describe (список таблиц)
\dt - Describe Tables
\dv - Describe Views
\di - Describe Indexes
\d имя_таблицы - выведет таблицу

## Удаление таблицы

-удалить
DROP TABLE название_таблицы;

-удалить если существует
DROP TABLE IF EXIST название_таблицы;

## Изменение таблиц в SQL
ALTER - изменить

ALTER TABLE superheroes ADD COLUMN alive BOOLEAN;

ALTER TABLE superheroes DROP COLUMN year;

ALTER TABLE superheroes RENAME COLUMN name TO hero_name;


# 6 Вставка и изменение данных в SQL

## Кратко

Ключевые слова:
    - INSERT
    - UPDATE
    - DELETE

Особенности:
    - Один оператор может менять несколько строк данных
    - Фильтры WHERE так же как и в SELECT
    - Первичный ключ позволяет однозначно идентифицировать строки

## Вставка данных

INSERT INTO superheroes(name, appearances)
VALUES ('Spider-Man, 4043)

## Изменение данных 

UPDATE superheroes
SET name='Batman',
    universe='dc'
WHERE id=1


UPDATE superheroes
SET gender='Man',
WHERE gener='Male%'

## Удаление данных

-удалить строку

DELETE FROM superheroes
WHERE id=2

- удалить строки по фильтру

DELETE FROM superheroes
WHERE gender='Male Characters'

- удалить все строки в таблице

DELETE FROM superheroes


# 7 Группировка данных в SQL: GROUP BY

## Кратко

Ключевые слова:
    - GROUP BY
    - COUNT(*) AS alias - делаем подсчет и именуем колонку

Группировка и другие возможности:
    - Фильтрация: WHERE
    - Сортировка: ORDER BY
    - Ограничения строк: LIMIT
    - Фильтрация после группировки: HAVING COUNT(*) - элиас нельзя, отрабатывает до присвоения

## Примергруппировки данных

SELECT universe, align, COUNT(*) AS total_heroes
FROM superheroes
GROUP BY universe, align 
HAVING COUNT(*) > 1000 
ORDER BY total_heroes DESC

 universe |      align      | total_heroes 
----------+-----------------+--------------
 marvel   | Bad Characters  |         2011
 marvel   | Good Characters |         1942
 dc       | Good Characters |         1245
(3 rows)


# 8 Группировка данных в SQL

## Кратко
- Агрегатные функции обрабатывают несколько строк и вычисляют одно значение.
- Используются вместе с группировкой (как правило)
- Поддерживают фильтрацию (WHERE), сортировку (ORDER BY), граничение (LIMIT)
- Фильтрация результатов группировки - HAVING

## Агрегатные функции:

- COUNT - количество.  всегда возвращает целое число (bigint)
- SUM - сумма значений
- AVG - среднее значение
- MAX - максимальное значение
- MIN - минимальное значе

## Примеры

SELECT align, COUNT(*), SUM(appearances)
FROM superheroes
GROUP BY align

       align        | count |  sum   
--------------------+-------+--------
 Good Characters    |  3187 | 209889
 Neutral Characters |  1169 |  42682
 Reformed Criminals |     2 |     83
 Bad Characters     |  2923 |  53539
(4 rows)


- С вычислением
    - ниже AVG - выдаёт 16 чисел после точки, а Оператор деления / возвращает целое число только тогда, когда оба числа (и делимое, и делитель) являются целыми. 

SELECT align, AVG(appearances),
    SUM(appearances)/COUNT(*) AS average
FROM superheroes
GROUP BY align


       align        |         avg         | average 
--------------------+---------------------+---------
 Good Characters    | 65.8578600564794478 |      65
 Neutral Characters | 36.5115483319076133 |      36
 Reformed Criminals | 41.5000000000000000 |      41
 Bad Characters     | 18.3164556962025316 |      18


- без группировки

SELECT COUNT(*),
    MIN(appearances),
    MAX(appearances),
    SUM(appearances),
    AVG(appearances)
FROM superheroes

 count | min | max  |  sum   |         avg         
-------+-----+------+--------+---------------------
  7281 |   1 | 4043 | 306193 | 42.0537014146408460


# 9 Группировка и фильтрация в SQL: HAVING

## Фильтрация данных

WHERE - фильтрация строк в таблице
HAVING - фильтрация результатов группировки

## Порядок выполнения SELECT

База данных обрабатывает запрос не сверху вниз, а в своей строгой логической последовательности.

1. Выбор таблицы: FROM
2. Фильтрация строк из таблицы: WHERE
3. Группировка: GROUP BY
4. Фильтрация результатов группировки: HAVING
5. Формирование для вывода: SELECT

## Проблемный пример

SELECT hair, COUNT(*)
FROM superheroes
WHERE gender='Female Characters'
    AND COUNT(*) > 10  # COUNT(*) еще не существует
GROUP BY hair

>>> ERROR: aggregate functions are not allowed in WHERE

## Фильтрация после группировки

SELECT hair, COUNT(*)
FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
HAVING COUNT(*) > 10    # работает с готовыми группами
LIMIT 5

         hair          | count 
-----------------------+-------
 Strawberry Blond Hair |    25
 Bald                  |    18
 Green Hair            |    42
 Red Hair              |   272
 White Hair            |    97


- вариант условия:
HAVING COUNT(*) BETWEEN 50 AND 300


# 10 Декомпозиция данных в базе

- Несколько таблиц в БД, причины:
    - Разные сущности
    - Декомпозиция одной таблицы на несколько

- Связи между таблицами
    - Ссылки из одной таблицы на другую
    - Внешний ключ FOREIGN KEY

- Проектирование БД
    - Нормализация: нормальные формы (требования как разбивать информацию на таблицы. 1, 2, 3...)
    - Типы связей:
        - один к одному
        - один ко многим
        - многие ко многим


# 11 Запрос данных из нескольких таблиц: JOIN

## Суть

- Запрос данных из нескольких таблиц
    - Оператор SELECT
    - В ключевом слове FROM указываем несколько таблиц с JOIN
    - После ключевого слова ON указываем условия объединения

- Связи между таблицами
    - Ссылки из одной таблицы на другую
    - Внешний ключ FOREIGN KEY

- Использование JOIN в SELECT
    - Комбинация с WHERE, ORDER BY, LIMIT, GROUP BY, HAVING
    - Типы JOIN: внешниее и внутреннее, левое и правое, перекрестное, полное

## Примеры внетреннего объединения

- Просто сливаем в одну + алиасы

SELECT *
FROM products AS p
JOIN product_types AS pt 
    ON p.type_id = pt.id

- Берем конкретные поля

SELECT 
    p.name AS product_name,
    pt.type_name AS product_type,
    p.price AS product_price
FROM products AS p 
JOIN product_types AS pt
ON p.type_id = pt.id
WHERE pt.type_name='Онлайн-курс'
    AND p.price > 10000
ORDER BY p.price DESC
LIMIT 10


               product_name                | product_type | product_price 
-------------------------------------------+--------------+---------------
 Инженерия искусственного интеллекта       | Онлайн-курс  |         60000
 Технологии обработки больших данных       | Онлайн-курс  |         50000
 Нейронные сети для анализа текстов        | Онлайн-курс  |         50000
 Нейронные сети для анализа изображений    | Онлайн-курс  |         50000
 Программирование глубоких нейронных сетей | Онлайн-курс  |         30000
 Основы искусственного интеллекта          | Онлайн-курс  |         15000


# 12 Типы JOIN в SQL

## Теория
- Внутреннее объединеие / INNER JOIN / JOIN (по умолчанию)
    - Включает строки, которым есть соответсвующие строки в другой таблице

- Внешнее объединение
    - значения могут отсутсвовать или не встречаться в обеих таблицах

    - LEFT OUTER JOIN
    - RIGHT OUTER JOIN
    - FULL OUTER JOIN

- Перекрестное объединение
    - CROSS JOIN
    - Не используется на практике

## LEFT и RIGHT OUTER JOIN

- LEFT OUTER JOIN
    - Внимание на пустую ячейку. Она пуста в products, но все равно вошла.

SELECT
p.name, pt.type_name
FROM products AS p
LEFT OUTER JOIN product_types AS pt
ON p.type_id = pt.id


                             name                              |  type_name  
---------------------------------------------------------------+-------------
 Основы искусственного интеллекта                              | Онлайн-курс
 Технологии обработки больших данных                           | Онлайн-курс
 Программирование глубоких нейронных сетей                     | Онлайн-курс
 Нейронные сети для анализа текстов                            | Онлайн-курс
 Нейронные сети для анализа изображений                        | Онлайн-курс
 Инженерия искусственного интеллекта                           | Онлайн-курс
 Как стать DataScientist'ом                                    | Вебинар
 Планирование карьеры в DataScience                            | Вебинар
 Области применения нейросетей: в какой развивать экспертность | Вебинар
 Программирование глубоких нейронных сетей на Python           | Книга
 Математика для DataScience                                    | Книга
 Основы визуализации данных                                    | Книга
 Анализ временных рядов                                        | 


- RIGHT OUTER JOIN
    - строка 4 - КОнсультация из pt вошла в таблицу, а строка без типа из p - нет

SELECT
p.name, pt.type_name
FROM products AS p
RIGHT OUTER JOIN product_types AS pt
ON p.type_id = pt.id


                             name                              |  type_name   
---------------------------------------------------------------+--------------
 Основы искусственного интеллекта                              | Онлайн-курс
 Технологии обработки больших данных                           | Онлайн-курс
 Программирование глубоких нейронных сетей                     | Онлайн-курс
 Нейронные сети для анализа текстов                            | Онлайн-курс
 Нейронные сети для анализа изображений                        | Онлайн-курс
 Инженерия искусственного интеллекта                           | Онлайн-курс
 Как стать DataScientist'ом                                    | Вебинар
 Планирование карьеры в DataScience                            | Вебинар
 Области применения нейросетей: в какой развивать экспертность | Вебинар
 Программирование глубоких нейронных сетей на Python           | Книга
 Математика для DataScience                                    | Книга
 Основы визуализации данных                                    | Книга
                                                               | Консультация


- LEFT и RIGHT OUTER JOIN можно переделать друг в друга поменям местами слогаемые.
Из-за этого RIGHT OUTER JOIN используют редко

- LEFT

SELECT
p.name, pt.type_name
FROM product AS p
LEFT OUTER JOIN product_types AS pt
ON p.type_id = pt.id


- RIGHT

SELECT
p.name, pt.type_name
FROM product_types AS pt
RIGHT OUTER JOIN products AS p
ON pt.id = p.type_id


## FULL OUTER JOIN

- включает строки из обеих

SELECT p.name, pt.type_name
FROM products AS p
FULL OUTER JOIN product_types AS pt
ON p.type_id = pt.id

                             name                              |  type_name   
---------------------------------------------------------------+--------------
 Основы искусственного интеллекта                              | Онлайн-курс
 Технологии обработки больших данных                           | Онлайн-курс
 Программирование глубоких нейронных сетей                     | Онлайн-курс
 Нейронные сети для анализа текстов                            | Онлайн-курс
 Нейронные сети для анализа изображений                        | Онлайн-курс
 Инженерия искусственного интеллекта                           | Онлайн-курс
 Как стать DataScientist'ом                                    | Вебинар
 Планирование карьеры в DataScience                            | Вебинар
 Области применения нейросетей: в какой развивать экспертность | Вебинар
 Программирование глубоких нейронных сетей на Python           | Книга
 Математика для DataScience                                    | Книга
 Основы визуализации данных                                    | Книга
 Анализ временных рядов                                        | 
                                                               | Консультация


## CROSS JOIN (каждая с каждой)
- условие не пишем, итоговая таблица содержит перекрестные соотношения
- на практике используется редко

SELECT products.name, product_types.type_name
FROM products
CROSS JOIN product_types
ORDER BY products.name


                            name                              |  type_name   
---------------------------------------------------------------+--------------
 Анализ временных рядов                                        | Консультация
 Анализ временных рядов                                        | Книга
 Анализ временных рядов                                        | Вебинар
 Анализ временных рядов                                        | Онлайн-курс
 Инженерия искусственного интеллекта                           | Вебинар
 Инженерия искусственного интеллекта                           | Консультация
 Инженерия искусственного интеллекта                           | Книга
 Инженерия искусственного интеллекта                           | Онлайн-курс
 Как стать DataScientist'ом                                    | Онлайн-курс
 Как стать DataScientist'ом                                    | Вебинар
 Как стать DataScientist'ом                                    | Книга
...
(53 rows)


# 13 Схема базы данных

## Теория

- Схемы базы даннных
    - Таблицы
    - Столбцы в таблицах и типы данных в них
    - Связи между таблицами

- Типы связей между таблицами
    - Один к одному (one-to-one)
    - Один ко многим (one-to-many)
    - Многие к одному (many-to-one)
    - Многие ко многим (many-to-many, реализуется через отдельную таблицу)


## Примеры 

## Продукты в заказе

SELECT p.id,
    p.name,
    p.price,
    s.quantity,
    p.price * s.quantity AS total
FROM products AS p
    JOIN sales AS s
    ON p.id = s.product_id
WHERE s.order_id=2

 id |                        name                         | price | quantity | total 
----+-----------------------------------------------------+-------+----------+-------
 10 | Программирование глубоких нейронных сетей на Python |  1000 |        2 |  2000
 11 | Математика для DataScience                          |  2000 |        2 |  4000


## Все покупки заказчика

SELECT p.id,
    p.name,
    p.price,
    s.quantity,
    p.price * s.quantity AS total
FROM products AS p
    JOIN sales AS s
    ON p.id = s.product_id
    JOIN orders AS o
    ON o.id = s.order_id
WHERE o.customer_id=1

 id |                   name                    | price | quantity | total 
----+-------------------------------------------+-------+----------+-------
  3 | Программирование глубоких нейронных сетей | 30000 |        1 | 30000
  4 | Нейронные сети для анализа текстов        | 50000 |        1 | 50000


# 14 Подзапросы SQL

## Теория

- Подзапросы в SQL (subqueries)
    - подзапросы в скобках выполняются первыми
    - Оформляется в круглые скобки

- Есть еще коррелируемые подзапросы
    - похожи на циклы в питоне
    - для каждой строки выполняется запрос (пример есть ниже)

- Диагностика подзапроса
    - Запуск подзапроса отдельно от основного запроса

- Использование подзапросов в командах SQL
    - SELECT
    - UPDATE
    - DELETE
    - INSERT


## Примеры

### Вывод наиболее дорогого продукта

SELECT id, name, price
FROM products
WHERE price = (SELECT MAX(price) FROM products)

 id |                name                 | price 
----+-------------------------------------+-------
  6 | Инженерия искусственного интеллекта | 60000


### Вывод информации о продуктах, которые были проданы хотя бы один раз

- Мой вариант для практики

SELECT p.name, p.price, pt.type_name, SUM(s.quantity) AS total
FROM products AS p
JOIN product_types AS pt
ON p.type_id = pt.id
JOIN sales AS s
ON p.id = s.product_id
GROUP BY p.name, p.price, pt.type_name

                        name                         | price |  type_name  | total 
-----------------------------------------------------+-------+-------------+-------
 Инженерия искусственного интеллекта                 | 60000 | Онлайн-курс |     1
 Нейронные сети для анализа изображений              | 50000 | Онлайн-курс |     1
 Программирование глубоких нейронных сетей           | 30000 | Онлайн-курс |     2
 Основы искусственного интеллекта                    | 15000 | Онлайн-курс |     1
 Программирование глубоких нейронных сетей на Python |  1000 | Книга       |     2
 Нейронные сети для анализа текстов                  | 50000 | Онлайн-курс |     2
 Математика для DataScience                          |  2000 | Книга       |     2


- пример из курса

SELECT id, name, price
FROM products
WHERE id IN (SELECT product_id FROM sales)

 id |                        name                         | price 
----+-----------------------------------------------------+-------
  1 | Основы искусственного интеллекта                    | 15000
  3 | Программирование глубоких нейронных сетей           | 30000
  4 | Нейронные сети для анализа текстов                  | 50000
  5 | Нейронные сети для анализа изображений              | 50000
  6 | Инженерия искусственного интеллекта                 | 60000
 10 | Программирование глубоких нейронных сетей на Python |  1000
 11 | Математика для DataScience                          |  2000


### Подзапросы в UPDATE

UPDATE products
SET price = price + 500
WHERE type_id = (SELECT id
                FROM product_types
                WHERE type_name='Книга')


### Некоррелированный VS

- Обычный подзапрос (Некоррелированный)
Задача: Найти всех сотрудников, чья зарплата выше средней по всей компании.

SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees
);

Как это работает:
База данных выполняет внутренний запрос один раз.Получает одно число (например, 50000).Подставляет его в главный запрос: WHERE salary > 50000. Быстро выводит список подходящих людей. 

- Коррелированный подзапрос
Задача: Найти сотрудников, чья зарплата выше средней именно в их отделе

SELECT e1.name, e1.salary, e1.department_id
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary) 
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);

Как это работает:
Главный запрос берет первую строку (например, сотрудника Иванова из ИТ-отдела). Передает номер его отдела (e1.department_id) внутрь подзапроса. Подзапрос считает среднюю зарплату только для ИТ. Главный запрос сравнивает зарплату Иванова с этим результатом. Процесс повторяется для каждой следующей строки в таблице.


# 15 Транзакции в базах данных

## Причины невыполнения команд

- Отказ СУБД
    - Аппаратная проблема с сервером СУБД
    - Программная ошибка в СУБД или операционной системе
    - Не хватает места на диске для записи данных

- Отказ приложения пользователя
    - аппарат
    - программ
    - пользователь прервал работу приложения

- Потеря сетевого соединения клиента и сервера СУБД
    - аппарат
    - проблемы с работой сети

## Транзакции
- последовательность команд SQL, которые должны быть выполнены полностью или не выполнены вообще.

START TRANSACTION;

UPDATE accounts SET balance = balance - 15000
WHERE account_number = 1234567;

Update accounts SET balance = balance + 15000
WHERE account_number = 9876543;

COMMIT; # записываем в БД
ROLLBACK; # отмена изменений


## Автоматическая фиксация транзакций

- Авто фиксация транзакций
    - Спец режим работы СУБД
    - После выполнения каждой команды SQL автоматически фиксируется транзакция
    - НЕт возможности отменить измнения

- PostgreSQL - включено по умолчанию
- Oracle - выключено по умолчанию

- Рекомендуется отключить, что бы можно было откатить не обращаясь к администратору

## Завершение транзакций

- Команды COMMIT или ROLLBACK
    - явное подтверждение или отмена транзакции

- Запуск команд создания, изменения или удаления таблиц
    - команды выше не могут быть отменены.
    - перед их запуском предыдущая транзакция фиксируется

- Сбои
    - сервера
        - откат всех незавершенных транзакций после восстановления сервера
    - клиента 
        - откат незавершенной транзакции после тайм-аута


# 16 Индексы в базах данных

## Теория

- Индексы
    - Структура данных, позволяющая быстро определить положение интересующих данных в базе
    - Создается для столбца/ов в таблице
    - Обеспечивает возможность повысить производительность запросов
    - Используется автоматически СУБД если это эффективно
    - повышение производительности на чтение / снижение на запись

    - как алфавитный указатель в конце толстой книги или оглавление. Вместо того чтобы листать всю книгу с первой до последней страницы (Full Scan), СУБД смотрит в указатель, сразу находит нужную страницу и переходит к ней.

- Использование индексов
    - Быстрый поиск положения интересующих данных в таблице
    - Извлечение всех интересующих данных из таблицы по найденному положению
    Реализуется автоматически СУБД

### Когда может использоваься индекс

- для WHERE
- для JOIN
- для ORDER BY

### Порядок сортировки данных в индексе

CREATE INDES superheroes_appearances_idx
ON superheroes(appearances DESC)

### Индекс по нескольким столбцам

CREATE INDEX person_name_idx
ON person(last_name, first_name)

- использование. Оба:

SELECT *
FROM person
WHERE last_name = 'Sozykin'
    AND first_name = 'Andrey'

- использование. Первый ():
    - по второму не работает, так как отсортиррованно по первому.

SELECT *
FROM person
WHERE last_name = 'Sozykin'

### Удаление индекса

DROP INDEX person_name_idx

##  Теория +

- Главный алгоритм: B-Tree (Сбалансированное дерево)
    - Данные в дереве разветвляются по уровням. Вместо перебора миллионов строк СУБД делает всего 3–5 точечных переходов от корня дерева к «листьям» и находит нужную строку за доли миллисекунды.

- Основные виды индексов
    - Кластерный индекс (Clustered Index) Это сама таблица, физически отсортированная по ключу. У таблицы может быть только один кластерный индекс. Обычно это первичный ключ (PRIMARY KEY).
    - Некластерный индекс (Non-Clustered Index) Это отдельные «записные книжки» со ссылками на основную таблицу. Их можно создать много (например, по полям email, phone, created_at).
    - Составной индекс (Composite Index) Индекс сразу по двум или более столбцам (например, last_name + first_name). Важен порядок: он эффективно работает, только если вы ищете по первому столбцу или по обоим сразу.
    - Уникальный индекс (Unique Index) Не только ускоряет поиск, но и запрещает дубликаты (например, не даст зарегистрировать два одинаковых email).

- Какой ценой? (Минусы и компромиссы)
    - Замедление операций записи (INSERT, UPDATE, DELETE)
    - Потребление дискового пространства и ОЗУ
    - Фрагментация. 
        - приходится периодически обслуживать (делать REBUILD или REORGANIZE)

- Золотое правило использования - Создавайте индексы для: полей, которые часто стоят в блоках WHERE, JOIN, ORDER BY и GROUP BY. Не создавайте индексы для: таблиц, в которых мало строк (до нескольких сотен), или для столбцов с низкой уникальностью.


## Примеры

- создание индекса

CREATE INDEX superheroes_name_idx
ON superheroes(name)

- использование (авто)

SELECT name, appearances, eye, hair
FROM superheroes
WHERE name LIKE '%Iron Man%'


## Заметки на полях

### Проверка индекса: EXPLAIN

* EXPLAIN — показывает теоретический план запроса.
* EXPLAIN ANALYZE — выполняет запрос на самом деле и показывает точное время.
* Index Scan в ответе — отлично, индекс работает.
* Seq Scan в ответе — индекс игнорируется, идет полный перебор таблицы.

### Когда индекс НЕ работает (Seq Scan)

* Знак % в начале поиска: LIKE '%Man'. Блок B-Tree сортирует данные только с первой буквы.
* Функции над полем: WHERE LOWER(name) = '...'. Функция меняет данные на лету, ломая логику индекса.
* Маленькая таблица: Если в таблице мало строк, базе быстрее прочесть её всю целиком, чем тратить время на индекс.
* Много совпадений: При поиске WHERE name != 'Batman' или выборке >20% всей таблицы базе проще отсканировать всё подряд.

### Как это исправить

* Для поиска по середине слова (%Man%) — используйте специальный индекс GIN вместо B-Tree.
* Для поиска без учета регистра — создавайте индекс по выражению: CREATE INDEX ... ON superheroes (LOWER(name)).


# 17 Ограничения в базах данных SQL

- PRIMARY KEY -  первичный ключ 
- FOREIGN KEY - внешний ключ
- NOT NULL - не пустые значения 
- UNIQUE - уникальные значения
- CHECK - проверка условий 

- Ограничения на уровне таблицы
    - PRIMARY KEY(product_id, order_id)
    - CONSTRAINT positive_price CHECK (price >= 0)


CREATE TABLE superheroes(
    id INT PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    align VARCHAR(30) NOT NULL,
    eye VARCHAR(30) UNIQUE NOT NULL
)

- Первичный ключ из нескольких полей - составной ключ
    - Уникальной должна быть комбинация значений, а не каждое поле по отдельности.
    - Запрет на NULL: Ни product_id, ни order_id не могут быть пустыми (NULL)
    - часто используется в промежуточных таблицах (связь «многие ко многим»)

CREATE TABLE sales(
    product_id INT,
    order_id INT,
    quantity INT,
    PRIMARY KEY(product_id, order_id)
)

- Ограничения по проверке значений 

CREATE TABLE products(
    id PRIMARY KEY,
    name VARCHAR(100),
    type_id INT,
    price INT CHECK (price >= 0)
)

- Именованные ограничения (в переводе CONSTRAINT)

CREATE TABLE products(
    ...
    price INT CONSTRAINT positive_price
        CHECK (price >= 0)
)

- Ограничения на уровне таблицы

CREATE TABLE products(
    ...
    PRICE INT,
    CONSTRAINT positive_price CHECK (price >= 0)
)

-Ограничения ссылочной целостности / внешнего ключа

CREATE TABLE products(
    ...
    type_id INT REFERENCES product_types(id),
    price INT
)

- Действия при удалении

    - RESTRICT - запрет
    - CASCADE - удаление строк в связанных таблицах

CREATE TABLE products(
    ...
    type_id INT REFERENCES product_types(id),
        ON DELETE/UPDATE RESTICT / CASCADE ,
    price INT
)

- Внешний ключ на уровне таблицы

CREATE TABLE products(
    ...
    FOREIGN KEY(type_id) REFERECES product_types(id)
)

- Первичный и внешний ключи

CREATE TABLE sales(
    product_id INT REFERENCES products(id)
    product_id INT REFERENCES orders(id)
    quantity INT,
    PRIMARY KEY(product_id, order_id)
)


# Представления в SQL

## Теория 

- Представления
    - псевдонимы для запросов SELECT
    - используются как аналоги таблиц
    - не содержат данных

- Использование представлений
    - ограничение доступа к данным
    - псевдонимы для сложных запросов
    - сокрытие реализации

- Материализованные представления
    - содержат данные
    - повышают скорость выполнения запросов
    - требуют актуализации
        - REFRESH MATERIALIZED VIEW customers_v; - с блокировкой
        - REFRESH MATERIALIZED VIEW CONCURRENTLY customers_v;
            - CONCURRENTLY - не блокирует на чтение. только в postgres(вроде). требует уникальный индекс у представления

## Примеры

###  VIEW из одной таблицы

CREATE VIEW cust_v (айди, имя)
AS SELECT id, name FROM customers;

 айди |       имя       
------+-----------------
    1 | Иван Петров
    2 | Петр Иванов
    3 | Тимофей Сергеев
    4 | Даша Корнеева
    5 | Иван Иван

### VIEW из нескольких таблиц

CREATE VIEW products_v
AS SELECT 
    p.id AS id,
    p.name AS product_name,
    t.type_name AS product_type,
    p.price AS prduct_price
FROM products AS p
JOIN product_types AS t
    ON p.type_id = t.id


# 19 Заключение

## Что изучено

- Таблицы и данные SQL
    - Работа с таблицами - CREATE / ALTER/DROP TABLE
    - Вставка и изменение данных - INSERT / UPDATE / DELETE

- Запросы к данным
    - запрос данных - SELECT / FROM / WHERE / ORDER BY / LIMIT
    - объединение данных из нескольких таблиц - JOIN
    - группировки - GROUP BY / HAVING
    - подзапросы ()
        - обычные (независимые)
        - коррелируемые (связанные)
    - представления VIEW
        - обычный - ссылки
        - MATERIALIZED VIEW - отпечаток
    
- Функции СУБД
    - согласованность данных в базе: транзакции и ограничения
    - повышение производительности запросов: индексы


## Что не изучено

- Возможности SQL
    - общие табличные выражения - COMMON TABLE EXPRESSIONS
    - оконные функции
    - иерархические и рекурсивные запросы
    - функции работы с датами, строками и т.п.

- Проектирование БД
    - реляционная теория/нормальные формы
    - проектирование схемы БД

- Системы управления базами данных
    - Внутреннее устройство/администрирование
    - Оптимизация производительности/большие объемы данных


## Что изучать дальше

- Практика SQL
    - плейлист с разбором
    - тренажеры SQL: leetcode.com, sql-ex.ru, sql-academy.org
    - задачи по работе

- SQL в рабочей среде
    - SQL в языках программироания
    - SQL Frameworks
    - ORM (Object-Relational Mapping)
    - SQL в аналитике (Tableau, Power BI, Exel ...)

- Средства SQL для предметной области
    - Аналитика - оконные функции