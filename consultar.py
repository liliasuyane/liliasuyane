#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('projetos.db')

cursor = conn.cursor()

cursor.execute("""select * from inscricoes""")

for linha in cursor.fetchall():
    print(linha)
    
conn.close()


