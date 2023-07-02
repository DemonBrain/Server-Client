import socket
import threading
import pandas as pd
import sqlite3
DATABASE_NAME = "gym.db"
conn = sqlite3.connect(DATABASE_NAME)

cursor = conn.cursor()
f = open('bd.sql')
sql = f.read()
cursor.executescript(sql)

cursor.execute("PRAGMA table_list")
print(cursor.fetchall())


host = 'localhost'
port = 5000
frm = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print(f"Server running on {host}:{port}")

#practica

clients=[]
opciones=["Register","Rutina","Catalogos"]
usernames=[]
rutinas=["Push","Pull"]
partes=["Biceps","Abdominales","Quadriceps"]

df = pd.read_csv("megaGymDataset.csv", usecols=['Title','Desc','BodyPart','Equipment'])
df_eat = pd.read_csv("Food and Calories.csv")
push=["Dumbbell preacher curl", "TBS Hammer Curl", "Hammer curl"]

def broadcast(message,_client):      #impide que el cliente se mande mesnaje a si mismo
    for client in clients:
          if client != _client:
               client.send(message)

def disconnect(client):
     while True:
          try:
               message = client.recv(1024)
               broadcast(message,client)
          except:
               index = clients.index(client)
               username = usernames[index]    
               message = f"ChatBot: {username} disconnected".encode(frm)
               broadcast(message,client)
               clients.remove(client)
               usernames.remove(username)
               client.close()
               break 

def register(client):
     while True:
               print(f"Entro def")
               client.send("@register".encode(frm))
               username = client.recv(1024).decode(frm)
               separo = username.split()
               #statement = "INSERT INTO Usuario(usuario, contrasena) VALUES (?, ?)"
               #cursor.execute(statement, [separo[0], separo[1]])

               #contra = "SELECT ID_usuario FROM Usuario WHERE usuario = ?"
               #cursor.execute(contra, [separo[0]])
               #id = cursor.fetchone()[0]

               #statement = "INSERT INTO InfoUser(ID_usuario, nombre, email, altura, genero, peso, grasa) VALUES (?, ?, ?, ?, ?, ? ,?)"
               #cursor.execute(statement, [id, separo[2], separo[3], separo[4], separo[5], separo[6], separo[7]])
               print(f"{separo}")
               usernames.append(username)
               print(f"Termino")
               break
    
def rutina(client):
     while True:
          client.send("@rutina".encode(frm))
          opcion = client.recv(1024).decode(frm)
          opcion = int(opcion)-1
          print(opcion)
          if opcion == 2:
              break
          
          if opcion == 1:
              ejercicio(client)
              break

          while True:
              musculo = client.recv(1024).decode(frm)
              if musculo == "YA":
                  break
              df_sel = df.loc[df['BodyPart'] == musculo]
              res = str(df_sel.sample(n=3))
              print(res.split())
              client.send(res.encode(frm))
              while True:
                   respu = client.recv(1024).decode(frm)
                   if respu == "No":
                     client.send(str(df_sel.sample(n=3)).encode(frm))
                   else:
                        #statement = "INSERT INTO Rutina(ID_info, nombre_rutina) VALUES (?, ?)"
                        #cursor.execute(statement, [..., ...])
                        break   
               


def ejercicio(client):
     while True:
          print(f"Entro ejercicio")
          client.send("@ejercicio".encode(frm))
          print(f"Entro ejercicio")
          rutina = client.recv(1024).decode(frm)
          rutina = int(rutina)-1
          i=0

          while True:
                client.send(push[i].encode(frm))
                print(push[i])
                confirm = client.recv(1024).decode(frm)
                separo = confirm.split()
                #statement = "INSERT INTO Ejercicio(ID_rutina, nombre_ejercicio, setss, repeticiones, peso, musculo, equipamiento) VALUES (?, ?, ?, ?, ?, ? ,?)"
                #cursor.execute(statement, [id, nombre, separo[1], separo[2], separo[3], musculo, equipamiento])
                if separo[0] == "No":
                     i=i+1
                else:
                     break

          break      

def catalogo(client):
     while True:
          print(f"Entro catalogo")
          client.send("@catalogo".encode(frm))
          cat = client.recv(1024).decode(frm)
          cat = int(cat)-1
          if cat == 0:
              todos_ejerc(client)
              break
          if cat == 1:
              todos_comida(client)
              break          



def todos_ejerc(client):
     while True:
          print(f"Entro catalogo ejercicio")
          client.send("@all_ejer".encode(frm))
          part = client.recv(1024).decode(frm)
          part = int(part)-1
          i=0

          while True:
               df_sel = df.loc[df['BodyPart'] == partes[part]]
               df_sel.reset_index(inplace = True, drop = True)
               while True:
                    print(i)
                    result = str(df_sel.iloc[i])
                    print(result)
                    client.send(result.encode(frm))
                    confirm = client.recv(1024).decode(frm)

                    if confirm == "Si":
                        i=i+1
                    else:
                       break

               break     
          break

def todos_comida(client):
     while True:
          print(f"Entro catalogo comida")
          client.send("@all_eats".encode(frm))
          i=0
          while True:
               while True:
                    print(i)
                    result = str(df_eat.iloc[i])
                    print(result)
                    client.send(result.encode(frm))
                    confirm = client.recv(1024).decode(frm)

                    if confirm == "Si":
                        i=i+1
                    else:
                       break

               break     
          break     
          
          

def conection():
    while True:
        client, address = server.accept()
        
        while True:
           client.send("@opciones".encode(frm))
           opcion = client.recv(1024).decode(frm)
           opcion = int(opcion)-1
   
           clients.append(client)
        
           print(f"{opcion}")
           print(opciones[opcion])
           if opciones[opcion] == "Register":
            print(f"Entro")
            register(client)
            print(f"Salio")

           if opciones[opcion] == "Rutina":
            print(f"Entro")
            rutina(client)
            print(f"Salio")            
            
           if opciones[opcion] == "Catalogos":
            print(f"Entro")
            catalogo(client)
            print(f"Salio")  
             
            print(f"siguio")             



        



conection()        