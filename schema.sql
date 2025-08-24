-- We’ll create tables that mirror the Kaggle Walmart dataset:

-- stores table
CREATE TABLE stores (
    store INT PRIMARY KEY,
    type VARCHAR(5),
    size INT
);

-- features table
CREATE TABLE features (
    store INT,
    date DATE,
    temperature FLOAT,
    fuel_price FLOAT,
    markdown1 FLOAT,
    markdown2 FLOAT,
    markdown3 FLOAT,
    markdown4 FLOAT,
    markdown5 FLOAT,
    cpi FLOAT,
    unemployment FLOAT,
    is_holiday BOOLEAN,
    PRIMARY KEY (store, date)
);

-- train table
CREATE TABLE train (
    store INT,
    dept INT,
    date DATE,
    weekly_sales FLOAT,
    is_holiday BOOLEAN,
    PRIMARY KEY (store, dept, date)
);

-- test table
CREATE TABLE test (
    store INT,
    dept INT,
    date DATE,
    is_holiday BOOLEAN,
    PRIMARY KEY (store, dept, date)
);

-- We’ll run this automatically from Python next.