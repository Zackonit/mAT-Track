
import socket,threading
from LEDs import matrix_photons
from time import strftime
import optparse,sys

vectorBreakpoint = ['www.facebook.com','www.twitter.com',
                    'www.reddit.com','www.pornhub.com',
                    'www.santander.com','www.bancomer.com',
                    'www.bbva.com',"face","twi","ban"]

class threadingConnections:
    def intervalSocket(self,ipVector,target,lkive,file_system):
        self.socket_Family=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.file_system=file_system
        self.socket_Family.bind((ipVector,target))
        print(strftime('[%I:%M:%S] ')+'AF_INET: '+ ipVector,'target:',target,'\n',self.socket_Family)
        self.socket_Family.listen(lkive)
        
        self.connections,self.system_Addr=self.socket_Family.accept()
        print(strftime('[%I:%M:%S] ')+"intercept: %s Country: %s range: %s size:kbs(4b)" %(self.system_Addr[0],"Mexico","4"))
        self.info_size=self.connections.recv(2**10).decode("utf-8")
    
    def intoxicateFile_system(self,hexabytes=4096):
        with open(self.file_system,'w') as self.bytes_k:
            self.bytes_k.write(self.info_size)
            self.bytes_k.close()
        
        with open(self.file_system) as x:
            for line in x:
                for fx in vectorBreakpoint:
                    if fx in line:
                        msg=strftime('[%I:%M:%S] ')+"Intercept: %s in %s Country: %s" %(fx,self.system_Addr[0],"México[MEX]")
                        msg=str(msg)
                        matrix_photons.matrix_reaction(True,msg,"w")
                        print(self.socket_Family)
                        
        y=input("[*]Watch Information(Y/N): ")
        if y == 'y'.upper():
            print(self.info_size)
        else:
            self.socket_Family.close()
            sys.exit()


args=optparse.OptionParser()

args.add_option("-v","--ip",dest="ipVector",help="Example: 192.168.1.x")
args.add_option("-t","--target",dest="target",type="int",help="Example: target=8080")
args.add_option("-l","--live",dest="lkive",type="int",help="Example: listen(2)")
args.add_option("-f","--filesystem",dest="file_system",help="Example: args(0)")

(options,arguments) = args.parse_args()

ipVector = options.ipVector
target=options.target
lkive=options.lkive
file_system=options.file_system

if __name__ == "__main__":
    threadsSTREAM=threadingConnections() 
    if ipVector == None and target == None and lkive == None and file_system==None:
        print("Error: Not parameters in function f(x)")
        
    else:
        threadsSTREAM.intervalSocket(ipVector,target,lkive,file_system)
        threadsSTREAM.intoxicateFile_system()

