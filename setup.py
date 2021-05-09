#!/usr/bin/python
# -*- coding: latin-1 -*-
# TS3/5 New version server auto installer - NOT RUN ROOT USER VPS!!
# #TS3/5 IP : NinjaNetWork
import os
os.system('wget https://files.teamspeak-services.com/releases/server/3.13.3/teamspeak3-server_linux_amd64-3.13.3.tar.bz2')
os.system('tar -xvf teamspeak3-server_linux_amd64-3.12.0.tar.bz2')
os.system('rm teamspeak3-server_linux_amd64-3.12.0.tar.bz2')
os.system('echo "license_accepted=1" > teamspeak3-server_linux_amd64/.ts3server_license_accepted')
os.system('bash teamspeak3-server_linux_amd64/ts3server_startscript.sh start')
print "-----------=[ \033[91mHost/\033[94m TS5 Server Kuruldu! ]=-----------"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
print "          ....................................\033[94m "
print "          .  [+] \033[91mCode :\033[94mT13R / T i e r *      "
print "          . [+] \033[91mWeb :\033[94m Obir.Ninja"
print "          .[+] \033[91mGithub :\033[94mgithub.com/obir.ninja . "
print "          ....................................  " 
