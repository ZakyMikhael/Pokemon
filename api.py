#!/usr/bin/Python3

import mysql.connector
import hug



@hug.get('/') # <-- This is the only additional line
def all():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
    cursor = conn.cursor(buffered=True)
    cursor.execute("""SELECT * FROM pokedex""")
    result = cursor.fetchall()
    conn.close()
    return result

@hug.post('/')
def post():
    cursor.execute("""SELECT * FROM pokedex""")
    result = cursor.fetchall()
    conn.close()
    return result

@hug.put('/')
def my_func(name):
    name += ""
    return name

