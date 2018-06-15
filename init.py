#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import mysql.connector, tabulate, requests

conn = mysql.connector.connect(host="localhost",user="root",password="", database="pokemon")
cursor = conn.cursor(buffered=True)



cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokedex
        (
           id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
           id_pokedex int (100),
           name VARCHAR(100),
           type VARCHAR (100),
           Total int (100),
           HP int (100),
           attack int(100),
           Defense int(100),
           Sp_att int(100),
           SP_Def int(100),
           Speed int(100)

        );
    """)
conn.commit()

url = "https://pokemondb.net/pokedex/all"
reponse = requests.get(url)
html = str(reponse.content)
soup = BeautifulSoup (html, "html.parser")
table=soup.find (id = "pokedex")

for row in table.findAll("tr"):
    t = []
    for l in row.find_all ("td"):
        t.append(l.text)

    if len(t) > 1 :
        list = (t[(0)], t[(1)], t[(2)], t[(3)], t[(4)], t[(5)], t[(6)], t[(7)], t[(8)], t[(9)])
        cursor.execute(
                """INSERT INTO pokedex (id_pokedex, name, type , Total, HP, attack, Defense, Sp_att, Sp_Def, Speed) 
                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", list)
        conn.commit()

    else:
        print ("vide")

conn.close()


