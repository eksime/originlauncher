from winreg import OpenKey, CloseKey, QueryValueEx, HKEY_LOCAL_MACHINE
from os import getenv
from subprocess import Popen
from shlex import split
#from xml.dom import minidom
from psutil import Process

from time import sleep

regKey = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Electronic Arts\EA Core")
originDir = QueryValueEx(regKey , r"EADM6InstallDir")[0] + "\\"
CloseKey(regKey)  
   
#xml = minidom.parse(getenv("APPDATA") + r"\origin\local.xml")
#itemlist = xml.getElementsByTagName('Setting')

#for s in itemlist :
#    if s.attributes["key"].value == "DownloadInPlaceDir":
#        originGamesDir = s.attributes["value"].value
#        break

proc = Popen([originDir + "Origin.exe", r"origin://launchgame/OFB-EAST:43437"])
origin = Process(proc.pid)

while len(origin.get_children()) == 0:
    sleep(0.1)

origin.get_children()[0].wait()
origin.kill()
