-- migrator up
-- SQL in this section is executed when the migration is applied.
INSERT INTO category (name, parent_id) VALUES
    ('Продукты', NULL),
    ('Мясо', 1),
    ('Сырое мясо', 2),
    ('Мясные продукты', 2),
    ('Сладости', 1),
    ('Книги', NULL),
    ('Одежда', NULL),
    ('Электроника', NULL),
    ('Обувь', 7),
    ('Молочные продукты', NULL);

INSERT INTO expense (amount, category_id, expense_date, added_date, comment) VALUES
    (1588.89, 7, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (3819.69, 6, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (3515.41, 7, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (777.89, 8, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (746.13, 3, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (1438.42, 5, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (4620.71, 1, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (4251.21, 5, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (3129.36, 5, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (4288.73, 6, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (392.01, 2, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (2447.93, 3, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (198.75, 6, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (235.57, 2, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (3469.4, 8, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (4521.62, 6, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (3860.12, 5, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (420.37, 1, CURRENT_DATE, CURRENT_TIMESTAMP, NULL),
    (1211.79, 2, CURRENT_DATE, CURRENT_TIMESTAMP, 'какой-то комментарий'),
    (4599.25, 3, CURRENT_DATE, CURRENT_TIMESTAMP, NULL);

INSERT INTO budget (amount, period) VALUES
    (1000, 'День'),
    (10000, 'Неделя'),
    (100000, 'Месяц'),
    (1000000, 'Год');

-- migrator down
-- SQL in this section is executed when the migration is rolled back.
DELETE FROM budget;
DELETE FROM expense;
DELETE FROM category;
