-- migrator up
-- SQL in this section is executed when the migration is applied.
CREATE TYPE period AS ENUM(
    'День',
    'Неделя',
    'Месяц',
    'Год'
);

CREATE TABLE IF NOT EXISTS category (
    id BIGSERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES category (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS expense (
    id BIGSERIAL PRIMARY KEY,
    amount REAL NOT NULL,
    category_id BIGINT,
    expense_date DATE NOT NULL,
    added_date TIMESTAMP NOT NULL DEFAULT NOW(),
    comment TEXT,
	FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS budget (
    id BIGSERIAL PRIMARY KEY,
    amount REAL NOT NULL,
    period period NOT NULL DEFAULT 'День'
);

-- migrator down
-- SQL in this section is executed when the migration is rolled back.
DROP TABLE IF EXISTS budget;
DROP TABLE IF EXISTS expense;
DROP TABLE IF EXISTS category;
DROP TYPE IF EXISTS period;
