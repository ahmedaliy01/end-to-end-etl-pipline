import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data.csv', encoding='latin1')
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

engine = create_engine("mysql+pymysql://root:root123@mysql-db-main:3306/TestDB")

df.to_sql(name='kaggle_data', con=engine, if_exists='replace', index=False)
print("ETL Completed Successfully!")