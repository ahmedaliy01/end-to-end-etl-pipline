import pymysql
import pandas as pd
connection = pymysql.connect(
    host='mysql-db-main',
    user='root',
    password='root123',
    database='employees',
    cursorclass=pymysql.cursors.DictCursor 
)

try:
    with connection.cursor() as cursor:

        sql_query = "SELECT * FROM employees.departments ;"
        
        cursor.execute(sql_query)
        
        results = cursor.fetchall()
        df = pd.DataFrame(results)
        
        print("--- Query Results ---")
        print(df)

finally:
    connection.close()