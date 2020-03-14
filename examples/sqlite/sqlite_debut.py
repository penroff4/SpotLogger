import sqlite3
import os

SPOTLOGGER_DB = os.getcwd()+"\data\SpotLogger.db"

conn = sqlite3.connect(SPOTLOGGER_DB)
cursor = conn.cursor()

table_name_sql = """
SELECT name FROM sql_master WHERE type='table'
"""

cursor.execute(table_name_sql)