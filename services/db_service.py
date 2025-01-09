import sqlite3

def execute_sql(sql_query):
    try:
        connection = sqlite3.connect("db/student.db")
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        return f"Error: {e}"
