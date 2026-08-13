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
    ALTER TABLE

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


## Агрегатные функции:

- COUNT, SUM, AVG, MAX, MIN


https://dzen.ru/video/watch/67b186a0d9fdf0086cc22043?collection=author%3A068246c2-0108-41d4-844c-60aed908ad35
