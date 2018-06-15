#!/usr/bin/Python3

import mysql.connector
import hug
from django.db import models


conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
cursor = conn.cursor(buffered=True)


@hug.get('/')
def allpoke():
    cursor.execute("""SELECT * FROM pokedex""")
    result = cursor.fetchall()
    return result

@hug.get('/')
def findbyid(name):
        cursor.execute("""SELECT * FROM pokedex WHERE name =%s """, [name])
        result = cursor.fetchone()
        return result
        return name

@hug.put('/')
def putid(id, name):
        cursor.execute("""UPDATE pokedex SET name =%s WHERE id =%s """, [name, id]);
        conn.commit()
        return id, name


@hug.delete('/')
def deletename(id):

    cursor.execute("""DELETE FROM pokedex WHERE id =%s""", [id])
    conn.commit()
    print(id)
    return id


@hug.post('/')
def postid (id, name):
        cursor.execute("""SELECT * FROM pokedex WHERE id =%s AND AND name =%s """, [id, name])
        res = cursor.fetchall()
        if res:
            print ("Pokemon existe")
        else:
            cursor.execute("""INSERT INTO pokedex id =%s AND name =%s """, [id, name]);
            conn.commit()
        return id, name
