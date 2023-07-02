import socket
import threading

host = 'localhost'
port = 5000
frm = 'utf-8'



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host,port))  #coneccion server

def recivir_mess():
    while True:
        try:
            message = client.recv(1024).decode(frm)

            if message == "@opciones":
                print("(1) Register \n(2) Rutina \n(3) Catalogos")
                opcion = input("Elige una opcion: ")
                client.send(opcion.encode(frm))

            if message == "@register":
                user = input("Enter you username: ") 
                contra = input("Enter you password: ")  
                nombre = input("Enter you name: ")
                email = input("Enter you email: ")
                altura = input("Enter you altura: ")
                genero = input("Enter you genero: ")
                peso = input("Enter you peso: ")
                grasa = input("Enter you grasa: ")
                all = user +" "+ contra +" "+ nombre +" "+ email +" "+ altura +" "+ genero +" "+ peso +" "+ grasa
                client.send(all.encode(frm)) 
            
            if message == "@ejercicio":
                print("(1) Push \n(2) Pull")
                opcion = input("Elige una opcion: ")
                client.send(opcion.encode(frm))
                while True:
                   msg = client.recv(1024).decode(frm)
                   print(msg + ":") 
                   peso = input("Peso: ")
                   repeticiones = input("Rep: ")
                   series = input("Series: ")
                   confirm = input("Listo? Si/No:")
                   final =confirm+ "" + peso + "" + repeticiones + "" + series
                   if confirm == "No":
                        client.send(final.encode(frm))
                   else:
                       client.send(final.encode(frm))
                       break
                   
            if message == "@rutina":
                print("(1) Nueva \n(2) Existente")
                opcion = input("Elige una opcion: ")
                client.send(opcion.encode(frm))
                if opcion == "1":
                   while True:
                      elec = input("Elige una musculo: ")
                      client.send(elec.encode(frm))
                      if elec == "YA":
                          break
                      
                      msg = client.recv(1024).decode(frm)
                      print(msg ) 
                      while True:
                         nuevo = input("Te gusta?Si/No: ")
                         if nuevo == "No":
                            client.send(nuevo.encode(frm))
                            msg = client.recv(1024).decode(frm)
                            print(msg ) 
                         else:
                            client.send(nuevo.encode(frm))
                            break              
                   
            if message == "@catalogo":
                print("(1) Ejercicios \n(2) Comida")
                opcion = input("Elige una opcion: ")
                client.send(opcion.encode(frm))      

            if message == "@all_ejer":
                print("(1) Biceps \n(2) Abdominales \n(3) Quadriceps")
                opcion = input("Elige una opcion: ")
                client.send(opcion.encode(frm))
                while True:    
                    msg = client.recv(1024).decode(frm)
                    print(msg)  
                    confirm = input("Siguiente? Si/No:")
                    if confirm == "Si":
                        client.send(confirm.encode(frm))
                  
                    else:
                       client.send(confirm.encode(frm))
                       break                       

            if message == "@all_eats":

                while True:    
                    msg = client.recv(1024).decode(frm)
                    print(msg)  
                    confirm = input("Siguiente? Si/No:")
                    if confirm == "Si":
                        client.send(confirm.encode(frm))
                  
                    else:
                       client.send(confirm.encode(frm))
                       break                        



        except:
            print("An error ocurred....")
            client.close()
            break


recivir_thread = threading.Thread(target=recivir_mess)
recivir_thread.start()                       
 
