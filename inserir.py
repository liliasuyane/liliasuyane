# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('projetos.db')
cursor = conn.cursor()

while (True):
    
    nome = input("digite um nome: ")
    
    email = input("digite um email: ")
    
    fone = input("digite um numero de telefone: ")
    
    continuar = int(input("deseja continuar? (0-sim; 1-não)"))
    
    cursor.execute("""insert into inscricoes (nome, email, fone) values (?,?,?)""", (nome, email, fone))  
    
    if(continuar==1) :
        break
        conn.close()
    
conn.commit()

cursor.execute("""select * from inscricoes""")

for linha in cursor.fetchall():
    print(linha)
    
conn.close()

