

matrix=("\x1b[1;34m","\x1b[1;33m","\x1b[1;36m","\x1b[1;32m","\x1b[1;35m","\033[0;30;47m")

class matrix_photons:
    def matrix_reaction(self,xyz,asign):
        matrix_asvage = {
            "Mercury_Hg":matrix[0]+xyz, 
            "PHtnasO": matrix[1] + xyz, 
            "h20_Universal": matrix[2] + xyz,
            "expOBomb": matrix[3] + xyz,
            "NaRgb": matrix[4] + xyz,
            "white": matrix[5] +xyz +"\033[0;m" 
            }   
        x,y,z,m,r,w= matrix_asvage["Mercury_Hg"], matrix_asvage["PHtnasO"],matrix_asvage["h20_Universal"],matrix_asvage["expOBomb"],matrix_asvage["NaRgb"], matrix_asvage["white"]

        if(asign == "x"): #blue
            print(x)
        
        if(asign == "y"): #yellow
            print(y)
        
        if(asign == "z"): #cian
            print(z)
        
        if(asign == "m"): #green
            print(m)
        
        if(asign == "r"):#purple
            print(r)
        
        if(asign=="w"):
            print(w)

    #def cLoggerMatTrack(self, action=True):
     #   matTrack_banner = """
        

      #        ███▄ ▄███▓▄▄▄█████▓▄▄▄█████▓ ██▀███   ▄████▄   ██ ▄█▀
       #      ▓██▒▀█▀ ██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▀ ▀█   ██▄█▒ 
        #     ▓██    ▓██░▒ ▓██░ ▒░▒ ▓██░ ▒░▓██ ░▄█ ▒▒▓█    ▄ ▓███▄░ 
         #    ▒██    ▒██ ░ ▓██▓ ░ ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓▓▄ ▄██▒▓██ █▄ 
          #   ▒██▒   ░██▒  ▒██▒ ░   ▒██▒ ░ ░██▓ ▒██▒▒ ▓███▀ ░▒██▒ █▄
           #  ░ ▒░   ░  ░  ▒ ░░     ▒ ░░   ░ ▒▓ ░▒▓░░ ░▒ ▒  ░▒ ▒▒ ▓▒
            # ░  ░      ░    ░        ░      ░▒ ░ ▒░  ░  ▒   ░ ░▒ ▒░
             #░      ░     ░        ░        ░░   ░ ░        ░ ░░ ░ 
             #░                        ░     ░ ░      ░  ░   
              #                        ░               


          #@zackonit.C0M-Put1nGClubCrypt0rs
        #"""
        #print(matTrack_banner)

        



