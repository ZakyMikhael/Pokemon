#!/usr/bin/Python3

import mysql.connector
import hug
import json
from django.db import models


conn = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")


@hug.get('/', output=hug.output_format.json)
def allpoks():
    cursor = conn.cursor(buffered=True)
    cursor.execute("""SELECT * FROM pokedex """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    ll = []
    for pokedex in results:
        ll.append(pokedex)
    return ll


@hug.put('/', output=hug.output_format.json)
def putid(id, name):
    cursor = conn.cursor(buffered=True)
    cursor.execute("""UPDATE pokedex SET name =%s WHERE id =%s """, [name, id]);
    conn.commit()
    return id, name


@hug.delete('/', output=hug.output_format.json)
def deletePokemon(pok):
    cursor = conn.cursor(buffered=True)
    print(pok.get("id"))
    try:
        cursor.execute("""DELETE FROM pokedex WHERE id_pokdex = %s""", [str(pok.get("id"))])
        conn.commit()
    except:
        return "ERROR"

    return json.dumps("good")


@hug.post('/', output=hug.output_format.json)
def postPokemon(b):
    values = []
    for i in b.values():
        values.append(i)

    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO pokemon (attack, defense, hp, name, pokedex_id, sp_atk, sp_def, speed, total) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", sorted(values))
        conn.commit()
    except:
        return "ERROR"

    return json.dumps("good")