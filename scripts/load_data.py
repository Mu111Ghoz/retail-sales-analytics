import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load DB credentials
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Create connection
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# === Step 1: Create Tables if not exist ===
schema_sql = """
CREATE TABLE IF NOT EXISTS stores (
    store INT PRIMARY KEY,
    type VARCHAR(5),
    size INT
);

CREATE TABLE IF NOT EXISTS features (
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

CREATE TABLE IF NOT EXISTS train (
    store INT,
    dept INT,
    date DATE,
    weekly_sales FLOAT,
    is_holiday BOOLEAN,
    PRIMARY KEY (store, dept, date)
);

CREATE TABLE IF NOT EXISTS test (
    store INT,
    dept INT,
    date DATE,
    is_holiday BOOLEAN,
    PRIMARY KEY (store, dept, date)
);
"""

with engine.begin() as conn:
    for stmt in schema_sql.strip().split(";"):
        if stmt.strip():
            conn.execute(text(stmt))

print("✅ Tables created successfully!")

# === Step 2: Load CSVs into DB ===
data_path = os.path.join("data")

files = {
    "stores": "stores.csv",
    "features": "features.csv",
    "train": "train.csv",
    "test": "test.csv"
}

for table, file in files.items():
    df = pd.read_csv(os.path.join(data_path, file))
    
    # Convert 'Date' column to datetime
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    
    # Rename to lowercase for consistency
    df.columns = [c.lower() for c in df.columns]
    
    # Insert into SQL
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"✅ Loaded {file} into {table}")
