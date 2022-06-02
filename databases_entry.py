import csv
import psycopg2
import glob
from psycopg2 import sql
from datetime import datetime


conn = psycopg2.connect('postgres://oynkonierltdgy:2e6c52a982ebe5d83448dd0f2a0a59115d028e9e6d1d2a394c713953e13c87ba@ec2-107-22-238-112.compute-1.amazonaws.com:5432/da7522agbf56fl')
cur = conn.cursor()

# insert_query = "INSERT INTO use(text) VALUES %s" , (a)
# cur.execute("INSERT INTO use(text) VALUES {} ".format(a))



value = [] 
{value.append(file.split('\\')[1].split('.')[0]) for file in glob.glob("w_seltexts\*.txt")} 


# cur.execute(sql.SQL("INSERT INTO {} VALUES (%s)").format(sql.Identifier(c)),(b,))


# a = ['zazazaza','sdfsf']

# cur.execute(f"INSERT INTO use (words) VALUES  {a}")

# cur.execute('SELECT * FROM use')
# for i in cur.fetchall():
#     print(i)

# print(value)
# cur.execute("""CREATE TABLE use(
#     text text
#     )
#     """)

# conn.commit()

for lang in value:
# #     # id integer PRIMARY KEY,
# #     # print(lang)
#     cur.execute(f"""CREATE TABLE {lang}(
#         words text
# )
#         """)
#     conn.commit()
    start_time = datetime.now()
    with open('w_seltexts/{}.txt'.format(lang), 'r', errors='replace') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                line.replace('\n','')
                cur.execute(sql.SQL("INSERT INTO {}(words) VALUES (%s)").format(sql.Identifier(lang)),(line,))
                end_time = datetime.now()  #put end time where u want to cunt 
print('Duration: {}'.format(end_time - start_time))
                # cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(lang)))
                # for i in cur.fetchone():
                #     print(i)
                # insert_query = "INSERT INTO {}(words) VALUES {}".format(lang,line)
                # cur.execute(insert_query)
                
#                 # cur.execute('SELECT * FROM de')
#                 cur.execute("INSERT INTO {}(text) VALUES {}".format(lang, line))
#             # cur.execute(f"INSERT INTO %s VALUES %s", (lang, line))


conn.commit()


# for lang in value:
# # from csv file insert into table
#     with open('languagecodeswords.csv', 'r') as f:
#         reader = csv.reader(f)
#         # next(reader)
#         # next(reader)
#         for row in reader:
#             # cur.execute("CREATE TABLE %s VALUES %s", (row) )
#             print(row[:15])

