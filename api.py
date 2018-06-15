#!/usr/bin/Python3

import mysql.connector
import hug

conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
cursor = conn.cursor(buffered=True)


@hug.get('/')
def allpoke():
    cursor.execute("""SELECT * FROM pokedex""")
    result = cursor.fetchall()
    return result

@hug.get('/')
def findbyid(tmp):
        cursor.execute("""SELECT * FROM pokedex WHERE id =%s """, [tmp])
        result = cursor.fetchall()
        return result
        return tmp
        conn.commit()

@hug.put('/')
def my_func(id):
    id += "55"
    return id


@hug.delete('/')
def deletename(tmp):

    cursor.execute("""DELETE FROM pokedex WHERE id =%s""", [tmp])
    conn.commit()
    print(tmp)
    return tmp


@hug.post('/')
def postid(id):
    cursor.execute ("""INSERT INTO pokedex (id) VALUES ("") """)
    conn.commit()
    conn.close()
