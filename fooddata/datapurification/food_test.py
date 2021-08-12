import sqlite3
import pandas as pd

# SQLite DB 연결
con = sqlite3.connect("./food.db")
 
# Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# SQL 쿼리 실행 테이블 불러오기
query = cur.execute("select * from pybo_food_data")
 
# 컬럼명지정
cols = [column[0] for column in query.description]
food_list = pd.DataFrame.from_records(data=query.fetchall(),columns=cols)

find_row = food_list.loc[food_list['food_name'] == '유과']

print(find_row)

# Connection 닫기
con.close()