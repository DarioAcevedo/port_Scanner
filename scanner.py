# Escaneador de puertos
import socket       
import sys


#Solicitamos y validamos la IP

ip = input("Introduce IP : ")

validateIP = ip.split('.')
validIP = True

for bit in validateIP:
    if int(bit) > 256 or int(bit) < 0:
        validIP = False
if validIP == False:
    print("Introduce una IP válida")
else:
    
    #Pedimos y validamos los puertos
    start = int(input("Introduce puerto de inicio : ")) 
    end = int(input("Introduce puerto de fin : "))      

    if (start > 65535 or start < 1) or (end > 65535 or end < 1):
        print("Por favor introduce un valor entre 1 y 65535")
    else:
        #Probamos los puertos
        print("Escaneando IP {} : ".format(ip))
        try:
        
            for port in range(start,end):                               # Bucle
                print ("Probando puerto {} ...".format(port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               # Crea el objeto socket
                s.settimeout(5)                                             # establecer timeout  
                if(s.connect_ex((ip,port))==0):                    # Comprobar conexion
                    print("Puerto " , port, "abierto")                   # Puerto abierto
                s.close()                                                       # Cierra el socket
            print("Escaneo finalizado!\n")
        
        except KeyboardInterrupt: 
            #Si se interrumpe el proceso manualmente
            print("Proceso Interrumpido, saliendo...")
            sys.exit()
        except socket.error:
            #Si no se pudo conectar con el servidor
            print("No se pudo conectar con el servidor, saliendo...")
            sys.exit()