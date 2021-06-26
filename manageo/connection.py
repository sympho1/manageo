import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as er:
		print(er)
	# finally:
	# 	if conn:
	# 		conn.close()
	return conn

def create_user(conn, sql_code):
	
	cur = conn.cursor()
	cur.execute(sql_code)
	conn.commit()
	# conn.close()


def create_table(conn, sql_code):
	try:
		cur = conn.cursor()
		cur.execute(sql_code)
	except Error as e:
		print(e)
	# finally:
	# 	if conn:
	# 		conn.close()

def get_user(conn, sql_code):
	cur = conn.cursor()
	cur.execute(sql_code)
	rows = cur.fetchall()
	for row in rows:
		print(row)

if __name__ == '__main__':
	sql_creat_user = """ insert into utilisateur values(
		"yao", "1234", "0748878646") """

	# conn = create_connection("db_file")
	# 


	sql_creat = """ create table if not exists utilisateur(
		nom varchar(250),
		password varchar(1000),
		phone varchar(50)
		) """

	conn = create_connection("mydb.sqlite")
	# creat_table(conn, sql_creat)
	# creat_user(conn, sql_creat_user)
	sel = """Select * from utilisateur"""
	get_user(conn , sel)
	conn.close()

# if __name__ == '__main__':
# 	create_connection("mydb.sqlite") #{Permet d'executer le programme et eviter son execution des que module}